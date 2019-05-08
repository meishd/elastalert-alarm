from aliyunsdkcore.request import RpcRequest
class SingleCallByTtsRequest(RpcRequest):

        def __init__(self):
                RpcRequest.__init__(self, 'Dyvmsapi', '2017-05-25', 'SingleCallByTts')

        def get_OutId(self):
                return self.get_query_params().get('OutId')

        def set_OutId(self,OutId):
                self.add_query_param('OutId',OutId)

        def get_CalledNumber(self):
                return self.get_query_params().get('CalledNumber')

        def set_CalledNumber(self,CalledNumber):
                self.add_query_param('CalledNumber',CalledNumber)

        def get_CalledShowNumber(self):
                return self.get_query_params().get('CalledShowNumber')

        def set_CalledShowNumber(self,CalledShowNumber):
                self.add_query_param('CalledShowNumber',CalledShowNumber)

        def get_TtsCode(self):
                return self.get_query_params().get('TtsCode')

        def set_TtsCode(self,TtsCode):
                self.add_query_param('TtsCode',TtsCode)

        def get_ResourceOwnerId(self):
                return self.get_query_params().get('ResourceOwnerId')

        def set_ResourceOwnerId(self,ResourceOwnerId):
                self.add_query_param('ResourceOwnerId',ResourceOwnerId)

        def get_OwnerId(self):
                return self.get_query_params().get('OwnerId')

        def set_OwnerId(self,OwnerId):
                self.add_query_param('OwnerId',OwnerId)

        def get_TtsParam(self):
                return self.get_query_params().get('TtsParam')

        def set_TtsParam(self,TtsParam):
                self.add_query_param('TtsParam',TtsParam)

        def get_ResourceOwnerAccount(self):
                return self.get_query_params().get('ResourceOwnerAccount')

        def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
                self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)
