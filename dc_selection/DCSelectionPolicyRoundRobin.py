"""
Title:          PyCloudSim
Description:    A Python-based Cloud Simulator
Author(s):      Mahmoud Momtazpour
Licence:        GPL - https://www.gnu.org/copyleft/gpl.html
Copyright (c) 2022-2023, Amirkabir University of Technology, Iran
"""

from dc_selection.DCSelectionPolicy import DCSelectionPolicy


class DCSelectionPolicyRoundRobin(DCSelectionPolicy):
    def __init__(self, datacenter_list):
        super().__init__(datacenter_list)
        self._vm_table = dict()
        self._last_selected = len(datacenter_list)-1

    def select_dc_for_vm(self, vm):
        return self._datacenter_list[(self._last_selected+1) % len(self._datacenter_list)]

    def reject_selection(self):
        self._last_selected = (self._last_selected + 1) % len(self._datacenter_list)

    def accept_selection(self):
        self._last_selected = (self._last_selected + 1) % len(self._datacenter_list)

