#
#    Uncomplicated VM Builder
#    Copyright (C) 2007-2008 Canonical
#    
#    See AUTHORS for list of contributors
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
from VMBuilder import register_hypervisor, Hypervisor
import VMBuilder
import os.path

class KVM(Hypervisor):
    name = 'KVM'
    arg = 'kvm'
    filetype = 'qcow2'

    def convert(self):
        for disk in self.vm.disks:
            target_img = '%s/%s.%s' % (self.vm.destdir, '.'.join(os.path.basename(disk.filename).split('.')[:-1]), self.filetype)
            self.vm.result_files.append(target_img)
            disk.convert(target_img, self.filetype)
    
register_hypervisor(KVM)
