from se34euca.testcase.testcase_base import *


class testcase_sequences(testcase_base):
    #sleep_time=30

    def instance_operations(self):
        sleep_time = 60
        print "=== runTest: Instance Operations ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.security_group.test_ui_create_security_group("mywebservice",
                                                                       "Rules for my webservice. Generated by Selenium")
        self.eucaUITester.security_group.test_ui_check_security_group_count("2")
        self.eucaUITester.keypair.test_ui_import_keypair_given_name("import-key")
        self.eucaUITester.keypair.test_ui_verify_keypair_given_name("import-key")
        self.eucaUITester.keypair.test_ui_check_keypair_count("1")
        self.eucaUITester.instance.test_ui_launch_instance_given_name_security_group_keypair("testinstance",
                                                                                             "mywebservice",
                                                                                             "import-key")
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
        self.eucaUITester.instance.test_ui_launch_instance_from_instances_lp("import-key")
        time.sleep(sleep_time)
        self.eucaUITester.instance.test_ui_check_running_instances_count("1")
        time.sleep(sleep_time)
        self.eucaUITester.instance.test_ui_launch_instance_from_images_lp("import-key")
        time.sleep(sleep_time)
        self.eucaUITester.instance.test_ui_check_running_instances_count("2")
        time.sleep(sleep_time)
        self.eucaUITester.instance.test_ui_terminate_instance_all()
        time.sleep(sleep_time)
        self.eucaUITester.instance.test_ui_check_running_instances_count("0")
        time.sleep(sleep_time)
        self.eucaUITester.security_group.test_ui_delete_security_group_all()
        self.eucaUITester.keypair.test_ui_delete_keypair_all()
        time.sleep(sleep_time)
        self.eucaUITester.keypair.test_ui_check_keypair_count("0")
        self.eucaUITester.base.test_ui_logout()
        time.sleep(sleep_time)

    def keypair_operations(self):
        sleep_time = 20
        print "=== runTest: Keypair Operations ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.keypair.test_ui_import_keypair_given_name("import-key")
        self.eucaUITester.keypair.test_ui_verify_keypair_given_name("import-key")
        self.eucaUITester.keypair.test_ui_check_keypair_count("1")
        self.eucaUITester.keypair.test_ui_delete_keypair_given_name("import-key")
        self.eucaUITester.keypair.test_ui_check_keypair_count("0")
        self.eucaUITester.keypair.test_ui_verify_delete_keypair_given_name("import-key")
        self.eucaUITester.keypair.test_ui_generate_keypair_given_name("my-sel-gen-key-00")
        self.eucaUITester.keypair.test_ui_verify_keypair_given_name("my-sel-gen-key-00")
        self.eucaUITester.keypair.test_ui_check_keypair_count("1")
        self.eucaUITester.keypair.test_ui_delete_keypair_all()
        self.eucaUITester.keypair.test_ui_check_keypair_count("0")
        self.eucaUITester.base.test_ui_logout()

    def security_group_operations(self):
        sleep_time = 60
        print "=== runTest: Security Group Operations ==="
        self.eucaUITester.base.test_ui_login()
        time.sleep(sleep_time)
        self.eucaUITester.security_group.test_ui_create_empty_security_group()
        time.sleep(sleep_time)
        self.eucaUITester.security_group.test_ui_check_security_group_count("2")
        time.sleep(sleep_time)
        time.sleep(sleep_time)
        self.eucaUITester.security_group.test_ui_check_security_group_sort()
        time.sleep(sleep_time)
        self.eucaUITester.security_group.test_ui_add_rules_to_security_group("test")
        time.sleep(sleep_time)
        time.sleep(sleep_time)
        self.eucaUITester.security_group.test_ui_create_security_group("mywebservice",
                                                                       "Rules for my webservice. Generated by Selenium")
        time.sleep(sleep_time)
        self.eucaUITester.security_group.test_ui_check_security_group_count("3")
        time.sleep(sleep_time)
        self.eucaUITester.security_group.test_ui_delete_security_group_all()
        time.sleep(sleep_time)
        self.eucaUITester.security_group.test_ui_check_security_group_count("1")
        time.sleep(sleep_time)
        self.eucaUITester.base.test_ui_logout()
        time.sleep(sleep_time)

    def ip_address_operations(self):
        print "=== runTest: IP Address Operations ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.keypair.test_ui_import_keypair_given_name("import-key")
        self.eucaUITester.keypair.test_ui_verify_keypair_given_name("import-key")
        self.eucaUITester.keypair.test_ui_check_keypair_count("1")
        self.eucaUITester.instance.test_ui_launch_instance_given_name_security_group_keypair("testinstance", "default", "import-key")
        self.eucaUITester.instance.test_ui_check_running_instances_count("1")
        self.eucaUITester.ip_address.test_ui_allocate_ip_address("1")
        self.eucaUITester.ip_address.test_ui_check_ip_address_count("1")
        available_ip = self.eucaUITester.ip_address.test_ui_get_available_ip_address()
        self.eucaUITester.instance.test_ui_associate_ip_given_instance_name_and_ip_address("testinstance", available_ip)
        self.eucaUITester.instance.test_ui_verify_associate_ip_given_instance_name_and_ip_address("testinstance", available_ip)
        #self.eucaUITester.instance.test_ui_associate_ip_from_inst_lp()
        self.eucaUITester.instance.test_ui_disassociate_ip_from_inst_lp()
        self.eucaUITester.instance.test_ui_associate_ip_from_ip_lp("testinstance")
        self.eucaUITester.instance.test_ui_disassociate_ip_from_ip_lp()
        self.eucaUITester.instance.test_ui_associate_ip_from_ip_lp("testinstance")
        self.eucaUITester.ip_address.test_ui_release_ip_address_all()
        self.eucaUITester.ip_address.test_ui_check_ip_address_count("0")
        self.eucaUITester.instance.test_ui_terminate_instance_all()
        self.eucaUITester.instance.test_ui_check_running_instances_count("0")
        self.eucaUITester.keypair.test_ui_delete_keypair_all()
        self.eucaUITester.keypair.test_ui_check_keypair_count("0")
        self.eucaUITester.base.test_ui_logout()

    def volume_operations(self):
        sleep_time = 60
        print "=== runTest: Volume Operations ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.keypair.test_ui_import_keypair_given_name("import-key")
        self.eucaUITester.keypair.test_ui_verify_keypair_given_name("import-key")
        self.eucaUITester.keypair.test_ui_check_keypair_count("1")
        self.eucaUITester.instance.test_ui_launch_instance_given_name_security_group_keypair("testinstance", "default", "import-key")
        self.eucaUITester.volume.test_ui_create_volume()
        time.sleep(sleep_time)
        self.eucaUITester.volume.test_ui_check_volume_count("1")
        self.eucaUITester.volume.test_ui_attach_volume()
        time.sleep(sleep_time)
        self.eucaUITester.volume.test_ui_detach_volume()
        self.eucaUITester.volume.test_ui_delete_volume_all()
        time.sleep(sleep_time)
        self.eucaUITester.keypair.test_ui_delete_keypair_all()
        time.sleep(sleep_time)
        self.eucaUITester.keypair.test_ui_check_keypair_count("0")
        self.eucaUITester.volume.test_ui_check_volume_count("0")
        self.eucaUITester.base.test_ui_logout()

    def volume_operations_02(self):
        sleep_time = 60
        print "=== runTest: Volume Operations 02 ==="
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.keypair.test_ui_import_keypair_given_name("import-key")
        self.eucaUITester.keypair.test_ui_verify_keypair_given_name("import-key")
        self.eucaUITester.keypair.test_ui_check_keypair_count("1")
        self.eucaUITester.instance.test_ui_launch_instance_given_name_security_group_keypair("testinstance", "default", "import-key")
        self.eucaUITester.volume.test_ui_create_volume_given_volume_name("test-volume")
        time.sleep(sleep_time)
        self.eucaUITester.volume.test_ui_attach_volume_from_instance_lp("test-volume")
        time.sleep(sleep_time)
        self.eucaUITester.volume.detach_volume_from_instance_lp("testinstance")
        time.sleep(sleep_time)
        self.eucaUITester.instance.test_ui_terminate_instance_all()
        time.sleep(sleep_time)
        self.eucaUITester.instance.test_ui_check_running_instances_count("0")
        self.eucaUITester.volume.test_ui_delete_volume_all()
        time.sleep(sleep_time)
        self.eucaUITester.keypair.test_ui_delete_keypair_all()
        time.sleep(sleep_time)
        self.eucaUITester.keypair.test_ui_check_keypair_count("0")
        self.eucaUITester.volume.test_ui_check_volume_count("0")
        self.eucaUITester.base.test_ui_logout()

    def snapshot_operations(self):
        sleep_time = 60
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.volume.test_ui_create_volume_given_volume_name("test-volume")
        time.sleep(sleep_time)
        self.eucaUITester.volume.test_ui_check_volume_count("1")
        self.eucaUITester.volume.test_ui_create_snapshot_from_volume()
        time.sleep(sleep_time)
        self.eucaUITester.snapshot.test_ui_check_snapshot_count("1")
        self.eucaUITester.snapshot.test_ui_create_volume_from_snapshot()
        time.sleep(sleep_time)
        self.eucaUITester.volume.test_ui_check_volume_count("2")
        self.eucaUITester.snapshot.test_ui_register_snapshot_as_image("test-image")
        time.sleep(sleep_time)
        self.eucaUITester.image.test_ui_check_image_count("2")
        self.eucaUITester.volume.test_ui_delete_volume_all()
        time.sleep(sleep_time)
        self.eucaUITester.volume.test_ui_check_volume_count("0")
        self.eucaUITester.snapshot.test_ui_delete_all_snapshots()
        time.sleep(sleep_time)
        self.eucaUITester.snapshot.test_ui_check_snapshot_count("0")
        self.eucaUITester.base.test_ui_logout()

    def xss_check_operations(self):
        sleep_time = 60
        print "=== runTest: XSS Check Operations ==="
        self.eucaUITester.base.test_ui_login()
        # CREATE A NEW KEYPAIR FOR LAUNCHING INSTANCE
        self.eucaUITester.keypair.test_ui_import_keypair_given_name("import-key")
        self.eucaUITester.keypair.test_ui_verify_keypair_given_name("import-key")
        self.eucaUITester.keypair.test_ui_check_keypair_count("1")
        # LAUNCH INSTANCE WITH AN XSS INJECTED INSTANCE NAME
        self.eucaUITester.instance.test_ui_launch_instance_given_name_security_group_keypair("<img src=x onerror=alert(1)>", "default", "import-key")
        # CREATE A VOLUME WITH AN XSS INJECTED VOLUME NAME
        self.eucaUITester.volume.test_ui_create_volume_given_volume_name("<img src=x onerror=alert(1)>")
        time.sleep(sleep_time)
        self.eucaUITester.instance.test_ui_check_running_instances_count("1")
        self.eucaUITester.volume.test_ui_check_volume_count("1")
        # CREATE A SNAPSHOT WITH AN XSS INJECTED SNAPSHOT NAME
        self.eucaUITester.volume.test_ui_create_snapshot_from_volume_given_snapshot_name("<img src=x onerror=alert(1)>", "<img src=x onerror=alert(1)>")
        time.sleep(sleep_time)
        self.eucaUITester.snapshot.test_ui_check_snapshot_count("1")
        # REGISTER THE SNAPSHOT AS AN IMAGE
        self.eucaUITester.snapshot.test_ui_register_snapshot_as_image("XSS-image")
        time.sleep(sleep_time)
        self.eucaUITester.image.test_ui_check_image_count("2")
        # NAME THE NEW IMAGE WITH AN XSS STRING
        self.eucaUITester.image.test_ui_tag_image_given_emi_name("XSS-image", "Name", "<img src=x onerror=alert(1)>")
        self.eucaUITester.image.test_ui_verify_emi_name_tag_given_image_name("XSS-image", "<img src=x onerror=alert(1)>")
        self.eucaUITester.base.test_ui_logout()


    def tagging_operations(self):
        sleep_time = 60
        self.eucaUITester.base.test_ui_login()
        self.eucaUITester.volume.test_ui_create_volume_given_volume_name("tag-test")
        time.sleep(sleep_time)
        self.eucaUITester.volume.test_ui_check_volume_count("1")
        self.eucaUITester.volume.test_ui_tag_volume_given_volume_name("tag-test", "1", "A")
        self.eucaUITester.volume.test_ui_tag_volume_given_volume_name("tag-test", "2", "B")
        self.eucaUITester.volume.test_ui_tag_volume_given_volume_name("tag-test", "3", "C")
        self.eucaUITester.volume.test_ui_verify_tag_given_volume_name("tag-test", "1", "A")
        self.eucaUITester.volume.test_ui_verify_tag_given_volume_name("tag-test", "2", "B")
        self.eucaUITester.volume.test_ui_verify_tag_given_volume_name("tag-test", "3", "C")
        self.eucaUITester.volume.test_ui_delete_volume_all()
        time.sleep(sleep_time)
        self.eucaUITester.volume.test_ui_check_volume_count("0")
        self.eucaUITester.base.test_ui_logout()


if __name__ == "__main__":
    unittest.main()

