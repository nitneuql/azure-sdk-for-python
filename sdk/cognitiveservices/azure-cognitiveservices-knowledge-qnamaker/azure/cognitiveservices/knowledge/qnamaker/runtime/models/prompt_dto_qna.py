# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .qn_adto import QnADTO


class PromptDTOQna(QnADTO):
    """QnADTO - Either QnaId or QnADTO needs to be present in a PromptDTO object.

    All required parameters must be populated in order to send to Azure.

    :param id: Unique id for the Q-A.
    :type id: int
    :param answer: Required. Answer text
    :type answer: str
    :param source: Source from which Q-A was indexed. eg.
     https://docs.microsoft.com/en-us/azure/cognitive-services/QnAMaker/FAQs
    :type source: str
    :param questions: Required. List of questions associated with the answer.
    :type questions: list[str]
    :param metadata: List of metadata associated with the answer.
    :type metadata:
     list[~azure.cognitiveservices.knowledge.qnamaker.runtime.models.MetadataDTO]
    :param context: Context of a QnA
    :type context:
     ~azure.cognitiveservices.knowledge.qnamaker.runtime.models.QnADTOContext
    """

    _validation = {
        'answer': {'required': True, 'max_length': 25000, 'min_length': 1},
        'source': {'max_length': 300},
        'questions': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'answer': {'key': 'answer', 'type': 'str'},
        'source': {'key': 'source', 'type': 'str'},
        'questions': {'key': 'questions', 'type': '[str]'},
        'metadata': {'key': 'metadata', 'type': '[MetadataDTO]'},
        'context': {'key': 'context', 'type': 'QnADTOContext'},
    }

    def __init__(self, **kwargs):
        super(PromptDTOQna, self).__init__(**kwargs)
