from rest_framework import serializers
from project.models import Project, Deliverable, SubDeliverable
import logging

class SubDeliverableSerializer(serializers.HyperlinkedModelSerializer):

    id = serializers.IntegerField(required=False)
    class Meta:
        model = SubDeliverable
        fields = ('id', 'sub_deliverable',)

#        read_only_fields = ('id', )


    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return SubDeliverable.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.deliverable = validated_data.get('sub_deliverable', instance.sub_deliverable)

        logging.debug("Validatdte SUB", validated_data)
        print("Validatdte SBU", validated_data)
        instance.save()
        return instance


class SubDeliverableListSerializer(serializers.ListSerializer):

    child = SubDeliverableSerializer()

    def create(self, validated_data):
        """
        Create and return a new `Deliverable` instance, given the validated data.
        """
        sub_deliverable_data = [SubDeliverable(deliverable=self.context.get('deliverable'), sub_deliverable=sub_deliverable.set(item.get('sub_deliverable'))) for item in validated_data]
        return SubDeliverable.objects.bulk_create(sbu_deliverable_data)


class DeliverableSerializer(serializers.HyperlinkedModelSerializer):

    sub_deliverables = SubDeliverableSerializer(many=True, required=False, allow_null=True)
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Deliverable
        fields = ('id', 'deliverable', 'sub_deliverables',)
        #read_only_fields = ('id', )


    def create(self, validated_data):
        """
        Create and return a new `Deliverable` instance, given the validated data.
        """
        return Deliverable.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.deliverable = validated_data.get('deliverable', instance.deliverable)

        instance.save()
        sub_deliverables = validated_data.get('sub_deliverables', None)
        if sub_deliverables:
            for sub_deliverable_data in sub_deliverables:
                sub_deliverable_id = sub_deliverable_data.get('id',None)
                if sub_deliverable_id:
                    sub_deliverable = SubDeliverable.objects.get(pk=sub_deliverable_id)
                    sub_deliverable.sub_deliverable = sub_deliverable_data.get('deliverable', deliverable.deliverable)
                else:
                    sub_deliverable = SubDeliverable.objects.create(deliverable=deliverable, sub_deliverable=sub_deliverable_data.get('sub_deliverable'))
                sub_deliverable.save()
        return instance

class DeliverableListSerializer(serializers.ListSerializer):

    child = DeliverableSerializer()

    def create(self, validated_data):
        """
        Create and return a new `Deliverable` instance, given the validated data.
        """
        final = []
        for dd in validated_data:
            #deliverable = Deliverable(project=self.context.get('project'), )
            deliverable = Deliverable.objects.create(project=self.context.get('project'),deliverable=dd.get('deliverable'))
            for sdd in dd.get('sub_deliverables'):
                #sub = SubDeliverable(deliverable=deliverable, sub_deliverable= sdd.get('sub_deliverable'))
                sub = SubDeliverable.objects.create(deliverable=deliverable, sub_deliverable=sdd.get('sub_deliverable'))
            final.append(deliverable)
        return final
        #return Deliverable.objects.bulk_create(deliverable_data)

    def update(self, instance, validated_data):
        """
        Create and return a new `Deliverable` instance, given the validated data.
        """
        final = []
        for dd in validated_data:
            #deliverable = Deliverable(project=self.context.get('project'), )
            deliverable = Deliverable.objects.create(project=self.context.get('project'),deliverable=dd.get('deliverable'))
            for sdd in dd.get('sub_deliverables'):
                #sub = SubDeliverable(deliverable=deliverable, sub_deliverable= sdd.get('sub_deliverable'))
                sub = SubDeliverable.objects.create(deliverable=deliverable, sub_deliverable=sdd.get('sub_deliverable'))
            final.append(deliverable)
        return final
class ProjectSerializer(serializers.HyperlinkedModelSerializer):

    deliverables = DeliverableSerializer(many=True, required=False,allow_null=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'start_date', 'duration', 'duration_type', 'active', 'deliverables')

        read_only_fields = ('id', )


    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Project.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.duration_type = validated_data.get('duration_type', instance.duration_type)
        instance.active = validated_data.get('active', instance.active)

        deliverables_data = validated_data.get('deliverables', None)
        logging.debug("Validatdte", validated_data)
        print("Validatdte", validated_data)
        instance.save()
        if deliverables_data:
            for deliverable_data in deliverables_data:
                logging.debug("Hello world", deliverable_data)
                print("Hello world", deliverable_data)
                deliverable_id = deliverable_data.get('id',None)
                logging.debug("Hello world adthe", deliverable_id)
                print("Hello world adthe", deliverable_id)
                if deliverable_id:
                    deliverable = Deliverable.objects.get(id=deliverable_id)
                    deliverable.deliverable = deliverable_data.get('deliverable', deliverable.deliverable)
                else:
                    deliverable = Deliverable.objects.create(project=instance, deliverable=deliverable_data.get('deliverable'))
                    #deliverable = Deliverable.objects.create(project=instance, **deliverable_data)
                deliverable.save()
                sub_deliverables = deliverable_data.get('sub_deliverables', None)
                if sub_deliverables:
                    for sub_deliverable_data in sub_deliverables:
                        sub_deliverable_id = sub_deliverable_data.get('id',None)
                        if sub_deliverable_id:
                            sub_deliverable = SubDeliverable.objects.get(id=sub_deliverable_id)
                            sub_deliverable.sub_deliverable = sub_deliverable_data.get('deliverable', deliverable.deliverable)
                        else:
                            sub_deliverable = SubDeliverable.objects.create(deliverable=deliverable, sub_deliverable=sub_deliverable_data.get('sub_deliverable'))
                        sub_deliverable.save()
        return instance

