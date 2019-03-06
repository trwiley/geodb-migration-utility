import sys
import migrationService

def main():
    geodbpath = sys.argv[1]
    connectpath = sys.argv[2]
    connectname = sys.argv[3]
    connectinstance = sys.argv[4]
    dbname = sys.argv[5]

    if connectname[-3:] != 'sde':
        raise Exception("workspace needs to be an .sde")

    ms = migrationService.migration_service(None, None, None, connectpath, connectname, connectinstance, dbname)

    ms.define_connection()
    ms.create_db_connection()
    ms.workspace = geodbpath
    ms.set_workspace()
    ms.transfer_feature_classes()

main()

