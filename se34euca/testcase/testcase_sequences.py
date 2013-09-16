from se34euca.testcase.testcase_base import *

class testcase_sequences(testcase_base):

    #sleep_time=30

    def instance_operations(self):
        sleep_time=60
        print "=== runTest: Instance Operations ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.instance.test_ui_launch_instance_given_name_security_group_keypair("testinstance","mywebservice","my-sel-gen-key-00")
        time.sleep(sleep_time)
        self.eucaUITester.instance.test_ui_check_running_instances_count("1")
        time.sleep(sleep_time)
        self.eucaUITester.instance.test_ui_launch_more_like_this()
        time.sleep(sleep_time)
        self.eucaUITester.instance.test_ui_check_running_instances_count("2")
        time.sleep(sleep_time)
        self.eucaUITester.instance.test_ui_terminate_instance_all()
        time.sleep(sleep_time)
        self.eucaUITester.instance.test_ui_check_running_instances_count("0")
        time.sleep(sleep_time)
        self.eucaUITester.instance.test_ui_launch_instance_from_instances_lp()
        time.sleep(sleep_time)
        self.eucaUITester.instance.test_ui_check_running_instances_count("1")
        time.sleep(sleep_time)
        self.eucaUITester.instance.test_ui_launch_instance_from_images_lp()
        time.sleep(sleep_time)
        self.eucaUITester.instance.test_ui_check_running_instances_count("2")
        time.sleep(sleep_time)
        self.eucaUITester.instance.test_ui_terminate_instance_all()
        time.sleep(sleep_time)
        self.eucaUITester.instance.test_ui_check_running_instances_count("0")
        time.sleep(sleep_time)
        self.eucaUITester.base.test_ui_logout()
        time.sleep(sleep_time)

    def keypair_operations(self):
        sleep_time=20
        print "=== runTest: Keypair Operations ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.keypair.test_ui_import_keypair()
        time.sleep(sleep_time)
        self.eucaUITester.keypair.test_ui_check_keypair_count("1")
        time.sleep(sleep_time)
        self.eucaUITester.keypair.test_ui_delete_keypair_given_name("import-key")
        time.sleep(sleep_time)
        self.eucaUITester.keypair.test_ui_check_keypair_count("0")
        time.sleep(sleep_time)
        self.eucaUITester.keypair.test_ui_generate_keypair_given_name("my-sel-gen-key-00")
        time.sleep(sleep_time)
        self.eucaUITester.keypair.test_ui_check_keypair_count("1")
        self.eucaUITester.base.test_ui_logout()
        time.sleep(sleep_time)

    def security_group_operations(self):
        sleep_time=40
        print "=== runTest: Security Group Operations ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.security_group.test_ui_create_empty_security_group()
        time.sleep(sleep_time)
        self.eucaUITester.security_group.test_ui_check_security_group_count("2")
        self.eucaUITester.base.test_ui_logout()
        time.sleep(sleep_time)

    def security_group_operations_01(self):
        sleep_time=60
        print "=== runTest: Security Group Operations 01==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.security_group.test_ui_delete_security_group_all()
        time.sleep(sleep_time)
        self.eucaUITester.security_group.test_ui_check_security_group_count("1")
        time.sleep(sleep_time)
        self.eucaUITester.security_group.test_ui_create_security_group()
        time.sleep(sleep_time)
        self.eucaUITester.security_group.test_ui_check_security_group_count("2")
        time.sleep(sleep_time)
        self.eucaUITester.base.test_ui_logout()
        time.sleep(sleep_time)

    def ip_address_operations(self):
        sleep_time=30
        print "=== runTest: IP Address Operations ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.instance.test_ui_launch_instance_given_name_security_group_keypair("testinstance","mywebservice","my-sel-gen-key-00")
        time.sleep(sleep_time)
        self.eucaUITester.instance.test_ui_check_running_instances_count("1")
        time.sleep(sleep_time)
        self.eucaUITester.ip_address.test_ui_allocate_ip_address("1")
        time.sleep(sleep_time)
        self.eucaUITester.ip_address.test_ui_check_ip_address_count("1")
        time.sleep(sleep_time)
        self.eucaUITester.instance.test_ui_associate_ip_from_inst_lp()
        self.eucaUITester.instance.test_ui_disassociate_ip_from_ip_lp()
        self.eucaUITester.instance.test_ui_associate_ip_from_ip_lp()
        #self.eucaUITester.instance.test_ui_disassociate_ip_from_inst_lp()
        #self.eucaUITester.instance.test_ui_associate_ip_from_ip_lp()
        self.eucaUITester.ip_address.test_ui_release_ip_address()
        self.eucaUITester.base.test_ui_logout()
        time.sleep(sleep_time)
if __name__ == "__main__":
    unittest.main()

