from se34euca.lib.EucaUITestLib_Base import *


class EucaUITestLib_Volume(EucaUITestLib_Base):
    def test_ui_gotopage_volumes(self):
        print
        print "Started Test: GotoPage Volumes"
        self.click_element_by_id("euca-logo")
        print
        print "Test: Received the Page Title -> " + self.driver.title
        self.click_element_by_id("dashboard-storage-volume")
        print
        print "Test: Clicked the GoToPage Button"
        self.verify_element_by_id("table-volumes-new")
        print
        print "Finished Test: GotoPage Volumes"
        print
        return 0

    def test_ui_create_volume(self):
        print
        print "Started Test: Create New Volume"
        print
        print "Test: Go to Dashboard"
        self.click_element_by_link_text("Dashboard")
        print "Test: Go to the Page Volume"
        self.click_element_by_id("dashboard-storage-volume")
        time.sleep(3)
        print
        print "Test: Create New Volume"
        self.click_element_by_id("table-volumes-new")
        self.set_keys_by_id("volume-size", "1")
        self.click_element_by_id("button-dialog-createvolume-save")
        print
        print "Finished Test: Create New Volume"
        print
        return 0

    def test_ui_create_volume_given_volume_name(self, volume_name):
        print
        print "Started Test: Create Volume Given Volume Name: " + str(volume_name)
        print
        print "Test: Go to the Page Volume"
        self.click_element_by_link_text("Dashboard")
        self.click_element_by_link_text("Storage")
        self.click_element_by_link_text("Volumes")
        time.sleep(3)
        print
        print "Test: Create a New Volume"
        self.click_element_by_id("table-volumes-new")
        self.set_keys_by_id("volume-name", str(volume_name))
        self.set_keys_by_id("volume-size", "1")
        self.click_element_by_id("button-dialog-createvolume-save")
        #Verifying on Volumes Landing Page that volume Named v was created
        print
        print "Verification"
        self.click_element_by_link_text(link_text="Dashboard")
        self.click_element_by_id("dashboard-storage-volume")
        time.sleep(3)
        self.verify_element_by_link_text(str(volume_name))
        print
        print "Finished: Create New Volume Given Volume Name: " + volume_name
        print
        return 0

    def test_ui_delete_volume(self):
        print
        print "Started Test: Delete Volume"
        print
        print "Test: Go to Dashboard"
        self.click_element_by_id("resource-menu-dashboard")
        print "Test: Go to the Page Volume"
        self.click_element_by_id("dashboard-storage-volume")
        time.sleep(3)
        self.click_element_by_css_selector("td.checkbox-cell > input[type=\"checkbox\"]")
        print
        print "Test: Delete Volume"
        self.click_element_by_id("more-actions-volumes")
        self.click_element_by_link_text("Delete")
        self.click_element_by_id("button-dialog-deletevolume-delete")
        print
        print "Finished: Delete Volume"
        print
        return 0

    def test_ui_delete_volume_all(self):
        print
        print "Started Test: Delete Volume All"
        print
        print "Test: Go to Dashboard"
        self.click_element_by_link_text("Dashboard")
        print "Test: Go to the Page Volume"
        self.click_element_by_id("dashboard-storage-volume")
        time.sleep(3)
        self.click_element_by_id("volumes-check-all")
        print
        print "Test: Delete Volume"
        self.click_element_by_id("more-actions-volumes")
        self.click_element_by_link_text("Delete")
        time.sleep(1)
        self.click_element_by_id("button-dialog-deletevolume-delete")
        print
        print "Finished: Delete Volume All"
        print
        return 0

    def test_ui_create_snapshot_from_volume(self):
        print
        print "Started Test: Create Snapshot From Volume"
        print
        print "Test: Go to Dashboard"
        self.click_element_by_id("resource-menu-dashboard")
        self.verify_element_by_link_text("Launch new instance")
        print
        print "Test: Go to the Page Volume"
        self.click_element_by_css_selector("#dashboard-storage-volume > span")
        time.sleep(3)
        self.verify_element_by_id("table-volumes-new")
        self.click_element_by_css_selector("td.checkbox-cell > input[type=\"checkbox\"]")
        print
        print "Test: Create Snapshot From Volume"
        self.click_element_by_id("more-actions-volumes")
        self.click_element_by_link_text("Create snapshot from volume")
        self.set_keys_by_id("snapshot-create-description", "Snapshot by Selenium Script")
        self.click_element_by_id("button-dialog-createsnapshot-save")
        print
        print "Finished: Create Snapshot From Volume"
        print
        return 0

    def test_ui_create_snapshot_from_volume_given_snapshot_name(self, snapshot_name, description = "Snapshot by Selenium Script"):
        print
        print "Started Test: Create Snapshot From Volume Given Snapshot Name"
        print
        print "Name: " + str(snapshot_name)
        print "Description: " + str(description)
        print
        print "Test: Go to the Dashboard"
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        print
        print "Test: Go to the Page Volume"
        self.click_element_by_link_text("Storage")
        self.click_element_by_link_text("Volumes")
        time.sleep(3)
        self.verify_element_by_id("table-volumes-new")
        self.click_element_by_css_selector("td.checkbox-cell > input[type=\"checkbox\"]")
        print
        print "Test: Create Snapshot From Volume"
        self.click_element_by_id("more-actions-volumes")
        self.click_element_by_link_text("Create snapshot from volume")
        self.set_keys_by_id("snapshot-create-name", str(snapshot_name))
        self.set_keys_by_id("snapshot-create-description", str(description))
        self.click_element_by_id("button-dialog-createsnapshot-save")
        #Verifying on Snapshots Landing Page that snapshot Named "snapshot_name" was created
        print
        print "Verification that snapshot " + snapshot_name + " is displayed on Snapshots Landing Page"
        self.click_element_by_link_text(link_text="Dashboard")
        self.click_element_by_id("dashboard-storage-snapshot")
        time.sleep(3)
        self.verify_element_by_link_text(str(snapshot_name))
        print
        print "Finished: Create Snapshot From Volume Given Snapshot Name"
        print
        return 0

    def test_ui_attach_volume(self):
        '''
        Attaches a volume to a running instance from Volumes Landing Page. Prerequisite: an instance named "testinstance"
        '''
        print
        print "Started Test: Attach Volume"
        print
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        print
        print "Test: Go to the Page Instances"
        self.click_element_by_link_text("Instances")
        self.click_element_by_css_selector("li.toggle-on > ul > li > a")
        time.sleep(3)
        self.click_element_by_link_text("testinstance")
        time.sleep(1)
        instance_id = self.get_text_by_xpath("//div[@id='tabs-1']/ul/li[2]/div[2]")
        self.click_element_by_link_text("Storage")
        self.click_element_by_link_text("Volumes")
        time.sleep(3)
        self.click_element_by_css_selector("div.table-row-status.status-available")
        self.click_element_by_id("more-actions-volumes")
        self.click_element_by_link_text("Attach to instance")
        self.set_keys_by_css_selector(
            "#volumes-attach-dialog-wrapper > #volumes-attach-dialog > div.dialog-inner-content > div.form-row > #volume-attach-instance-id",
            str(instance_id) + "testinstance")
        self.set_keys_by_id("volume-attach-device-name", "/dev/sdf")
        self.click_element_by_id("volumes-attach-dialog")
        self.click_element_by_id("button-dialog-attachvolume-save")
        print
        print "Verification by checking that there is a volume in attached state on Volumes Landing Page"
        print
        print "Click 'Dashboard' button"
        self.click_element_by_link_text("Dashboard")
        print "Click 'Storage' button"
        self.click_element_by_link_text("Storage")
        print "Click 'Volumes' from menu"
        self.click_element_by_link_text("Volumes")
        time.sleep(3)
        print "Verify there is an attached volume present"
        self.verify_element_by_css_selector("div.table-row-status.status-in-use")
        print
        print "Finished Test: Attach Volume"
        print

    def test_ui_check_volume_count(self, volumes_count):
        print
        print "Started Test: Check Volume Count"
        print
        self.click_element_by_link_text("Dashboard")
        self.verify_element_by_link_text("Launch new instance")
        print "Verifying that Volumes Count on Dashboard is " + volumes_count
        time.sleep(3)
        self.verify_text_displayed_by_css("#dashboard-storage-volume > span", volumes_count)
        print
        print "Finished Test: Check Volume Count"
        print
        return 0

    def test_ui_detach_volume(self):
        print
        print "Started Test: Detach Volume"
        print
        print "Click 'Dashboard' button"
        self.click_element_by_link_text("Dashboard")
        print "Click 'Storage' button"
        self.click_element_by_link_text("Storage")
        print "Click 'Volumes' from menu"
        self.click_element_by_link_text("Volumes")
        time.sleep(3)
        print "Check the volume in use"
        self.click_element_by_css_selector("div.table-row-status.status-in-use")
        print "Click the 'More actions' button"
        self.click_element_by_id('more-actions-volumes')
        print "Click 'Detach from instance' menu item"
        self.click_element_by_link_text("Detach from instance")
        print "Click 'Yes, detach' in the detach dialog"
        self.click_element_by_id("button-dialog-detachvolume-detach")
        print
        print "Verification by checking that there is no volume in attached state on Volumes Landing Page"
        print
        print "Click 'Dashboard' button"
        self.click_element_by_link_text("Dashboard")
        print "Click 'Storage' button"
        self.click_element_by_link_text("Storage")
        print "Click 'Volumes' from menu"
        self.click_element_by_link_text("Volumes")
        time.sleep(3)
        print "Verify volume detached by no volumes present in 'attached' state on the volumes page"
        self.verify_element_not_present("CSS_SELECTOR","div.table-row-status.status-in-use")
        print
        print "Finished Test: Detach Volume"
        print

    def test_ui_attach_volume_from_instance_lp(self, volume_name):
        '''
        Attaches volume by spacified name to a running instance
        '''
        print
        print "Started Test: Attach Volume from Instance Landing Page"
        print
        print "Click 'Dashboard' button"
        self.click_element_by_id("resource-menu-dashboard")
        print "Click 'Storage' button"
        self.click_element_by_id("resource-menu-storage")
        print "Click 'Volumes' from menu"
        self.click_element_by_id("resource-menuitem-volume")
        time.sleep(3)
        print "Clink on volume name 'test-volume' to open expando"
        self.click_element_by_link_text(volume_name)
        time.sleep(1)
        print "Store volume id of 'test-volume'"
        volume_id = self.get_text_by_xpath("//div[@id='tabs-1']/ul/li[2]/div[2]")
        print "Click 'Instances' button"
        self.click_element_by_id("resource-menu-instance")
        print "Click on 'Instances' menu item"
        self.click_element_by_id("resource-menuitem-instance")
        time.sleep(3)
        print "Check-box a running instance"
        self.click_element_by_css_selector("div.table-row-status.status-running")
        print "Click the 'More actions' menu"
        self.click_element_by_id("more-actions-instances")
        print "Click 'Attach volume' menu item"
        self.click_element_by_link_text("Attach volume")
        print "Verify the volume id field is visible in the 'Attach Volume' dialog"
        self.verify_element_by_id("volume-attach-volume-id")
        print "Type in volume id in the 'Attach Volume' dialog"
        self.set_keys_by_id("volume-attach-volume-id", volume_id + " ("+ volume_name + ")")
        print "Click the 'Attach' button"
        self.click_element_by_id("button-dialog-attachvolume-save")
        print "Go to Volume Landing Page"
        self.click_element_by_link_text("Dashboard")
        self.click_element_by_link_text("Storage")
        self.click_element_by_link_text("Volumes")
        time.sleep(3)
        print "Verify there is an attached volume present"
        self.verify_element_by_css_selector("div.table-row-status.status-in-use")
        print
        print
        print "Finished Test: Attach Volume from Instance Landing Page"
        print

    def detach_volume_from_instance_lp(self, instance_name):
        print
        print "Started Test: Detach Volume from Instance Landing Page"
        print
        print "Click 'Dashboard' button"
        self.click_element_by_id("resource-menu-dashboard")
        print "Click 'Instances' button"
        self.click_element_by_id("resource-menu-instance")
        print "Click 'Instances' from menu"
        self.click_element_by_id("resource-menuitem-instance")
        time.sleep(3)
        print "Clink " + instance_name + " to get instance id from expando"
        self.click_element_by_link_text(instance_name)
        time.sleep(1)
        instance_id = self.get_text_by_xpath("//div[@id='tabs-1']/ul/li[2]/div[2]")
        print "Check-mark " + instance_name
        self.click_element_by_id(instance_id)
        print "Click 'More actions'"
        self.click_element_by_id("more-actions-instances")
        print "Click 'Detach volume' on the menu"
        self.click_element_by_link_text("Detach volume")
        print "Click checkbox for an attached volume"
        self.click_element_by_css_selector('#volume-detach-grid > tbody > tr > td > input[type="checkbox"]')
        print "Click 'Detach' button"
        self.click_element_by_id("btn-vol-detach")
        print "Go to Volume Landing Page"
        self.click_element_by_link_text("Dashboard")
        self.click_element_by_link_text("Storage")
        self.click_element_by_link_text("Volumes")
        time.sleep(3)
        print "Verification by waiting for attached state to disappear from Volumes Landing page"
        self.verify_element_not_present("CSS_SELECTOR","div.table-row-status.status-in-use")
        print
        print "Finished Test: Detach Volume from Instance Landing Page"
        print

    def test_ui_get_volume_id_given_volume_name(self, volume_name):
        print
        print "Started VOLUME LANDING PAGE OPERATION: Return Volume ID Given Volume Name"
        print "Volume Name: " + volume_name
        print
        self.click_element_by_link_text(volume_name)
        time.sleep(3)
        volume_id = "NULL"
        volume_id = self.get_text_by_css_selector("ul.volume-expanded:nth-child(1) > li:nth-child(2) > div:nth-child(2)")
        print
        print "Finsihed VOLUME LANDING PAGE OPERATION: Return Volume ID Given Volume Name"
        print "Returning Volume ID: " + volume_id
        print
        return volume_id

    def test_ui_tag_volume_given_volume_name(self, volume_name, key, value):
        print
        print "Started Test: Tag Volume Given Volume Name"
        print "Volume Name: " + volume_name
        print "Key: " + key
        print "Value: " + value
        print
        print "Go to Volume Landing Page"
        self.click_element_by_link_text("Dashboard")
        self.click_element_by_link_text("Storage")
        self.click_element_by_link_text("Volumes")
        time.sleep(3)
        volume_id = self.test_ui_get_volume_id_given_volume_name(volume_name)
        self.click_element_by_id(volume_id)
        self.click_element_by_link_text("More actions")
        self.click_element_by_link_text("Manage tags")
        time.sleep(3)
        self.set_keys_by_id("inputbox_newtag_name", key)
        self.set_keys_by_id("inputbox_newtag_value", value)
        time.sleep(1)
        self.click_element_by_id("button-dialog-edittags-save")
        print
        print "Finished Test: Tag Volume Given Volume Name"
        print

    def test_ui_verify_tag_given_volume_name(self, volume_name, key, value):
        print
        print "Started Test: Verify Tag Given Volume Name"
        print "Volume Name: " + volume_name
        print "Key: " + key
        print "Value: " + value
        print
        print "Go to Volume Landing Page"
        self.click_element_by_link_text("Dashboard")
        self.click_element_by_link_text("Storage")
        self.click_element_by_link_text("Volumes")
        time.sleep(3)
        self.click_element_by_link_text(volume_name)
        time.sleep(3)
        self.click_element_by_link_text("Tags")
        time.sleep(1)
        match_string = str(key) + " " + str(value)
        is_found = False
        block = self.get_text_by_css_selector("#tabs-2")
        tags = block.split("\n")
        for tag in tags:
            print "Tag: " + tag
            if( tag == match_string ):
              print "Found the Tag."
              is_found = True
        if( is_found is False):
            print "FAILED Test: Verify Tag Given Volume Name"
            return 1
        print
        print "Finished Test: Verify Tag Given Volume Name"
        print
        return 0

if __name__ == "__main__":
    unittest.main()



