import sys
import migrationService

def main():
    workspace = sys.argv[1]
    folder_out = sys.argv[2]
    out_name = sys.argv[3]

    if workspace[-3:] != 'sde' :
        raise Exception("workspace needs to be an .sde")

    if out_name[-3:] != 'gdb':
        raise Exception("output file must be .gdb")

    ms = migrationService.migration_service(workspace, folder_out, out_name, None, None, None, None)      
    ms.set_workspace()
    ms.write_gdb()

main()


