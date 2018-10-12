import unittest
import testinfra


class Test(unittest.TestCase):

    def setUp(self):
        self.host = testinfra.get_host('docker://instance')
        self.namespace = "test"
        self.storageclass = "standard"

    def test_namespace_exist(self):
        namespaces = self.host.run('oc get namespaces')
        assert self.namespace in namespaces.stdout

    def test_storageclass_exist(self):
        storageclasses = self.host.run('oc get storageclass -n test')
        assert self.storageclass in storageclasses.stdout
