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

from msrest.serialization import Model


class PromptDTO(Model):
    """Prompt for an answer.

    :param display_order: Index of the prompt - used in ordering of the
     prompts
    :type display_order: int
    :param qna_id: Qna id corresponding to the prompt - if QnaId is present,
     QnADTO object is ignored.
    :type qna_id: int
    :param qna: QnADTO - Either QnaId or QnADTO needs to be present in a
     PromptDTO object
    :type qna:
     ~azure.cognitiveservices.knowledge.qnamaker.authoring.models.PromptDTOQna
    :param display_text: Text displayed to represent a follow up question
     prompt
    :type display_text: str
    """

    _validation = {
        'display_text': {'max_length': 200},
    }

    _attribute_map = {
        'display_order': {'key': 'displayOrder', 'type': 'int'},
        'qna_id': {'key': 'qnaId', 'type': 'int'},
        'qna': {'key': 'qna', 'type': 'PromptDTOQna'},
        'display_text': {'key': 'displayText', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PromptDTO, self).__init__(**kwargs)
        self.display_order = kwargs.get('display_order', None)
        self.qna_id = kwargs.get('qna_id', None)
        self.qna = kwargs.get('qna', None)
        self.display_text = kwargs.get('display_text', None)
