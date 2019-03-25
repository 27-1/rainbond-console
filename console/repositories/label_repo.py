# -*- coding: utf8 -*-
"""
  Created on 18/1/30.
"""
from www.models import ServiceLabels, NodeLabels, Labels


class ServiceLabelsReporsitory(object):
    def get_service_labels(self, service_id):
        return ServiceLabels.objects.filter(service_id=service_id)

    def delete_service_labels(self, service_id, label_id):
        ServiceLabels.objects.filter(service_id=service_id, label_id=label_id).delete()

    def delete_service_all_labels(self, service_id):
        ServiceLabels.objects.filter(service_id=service_id).delete()

    def get_service_label(self, label_id):
        return ServiceLabels.objects.filter(label_id=label_id).first()

    def get_labels_by_service_ids(self, service_ids):
        labels_list = ServiceLabels.objects.filter(service_id__in=service_ids)
        if labels_list:
            return labels_list
        else:
            return []


class NodeLabelsReporsitory(object):
    def get_node_label_by_region(self, region_id):
        return NodeLabels.objects.filter(region_id=region_id)

    def get_all_labels(self):
        labels = NodeLabels.objects.all()
        return labels


class LabelsReporsitory(object):
    def get_labels_by_label_ids(self, label_ids):
        return Labels.objects.filter(label_id__in=label_ids)

    def get_label_by_label_id(self, label_id):
        labels = Labels.objects.filter(label_id=label_id)
        if labels:
            return labels[0]
        return None

    def get_all_labels(self):
        labels = Labels.objects.all()
        return labels

    def get_labels_by_label_name(self, label_name):
        return Labels.objects.filter(label_name=label_name).first()


service_label_repo = ServiceLabelsReporsitory()
label_repo = LabelsReporsitory()
node_label_repo = NodeLabelsReporsitory()