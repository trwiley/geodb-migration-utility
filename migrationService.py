# migrationService
# service for operations related to migrating arcGIS geodatabases using the 
# following method:
#   1. convert to local file
#   2. convert the local file back into a geodatabase

import arcpy

class migration_service:
    def __init__(self, workspace, folder_out, out_name, connection_path, connection_name, connection_instance, database_name):
        self.__workspace = workspace
        self.__folderout = folder_out
        self.__outname = out_name
        self.__connectionpath = connection_path
        self.__connectionname = connection_name
        self.__connectioninstance = connection_instance
        self.__CONNECTION = {}
        self._databasename = database_name
    
    @property
    def workspace(self):
        return self.__workspace

    @workspace.setter
    def workspace(self, workspace):
        self.__workspace = workspace
    
    def set_workspace(self):
        arcpy.env.workspace = self.__workspace

    def write_gdb(self):
        # todo: clean this up a bit
        # create a list of feature classes in the workspace to 
        # transfer over to the newly created geodatabase
        arcpy.CreateFileGDB_management(self.__folderout, self.__outname)

        #print arcpy.ListFeatureClasses('', 'All', arcpy.ListDatasets()[0])
        geodbpath = self.__folderout + "\\" + self.__outname

        for f in arcpy.ListDatasets():
            fcList = arcpy.ListFeatureClasses('', 'All', f)
            if len(fcList) > 0:
                arcpy.FeatureClassToGeodatabase_conversion(fcList, geodbpath)

        fcList = arcpy.ListFeatureClasses()
        arcpy.FeatureClassToGeodatabase_conversion(fcList, geodbpath)


    def define_connection(self):
        self.__CONNECTION = {
            "path" : self.__connectionpath,
            "name" : self.__connectionname,
            "platform" : "SQL_SERVER",
            "instance" : self.__connectioninstance,
            "auth" : "OPERATING_SYSTEM_AUTH",
            "username" : "",
            "password" : "",
            "saveUserInfo" : "DO_NOT_SAVE_USERNAME",
            "databaseName" : self._databasenames,
            "versionName" : "SDE.DEFAULT",
            "saveVersionInfo" : "SAVE_VERSION"
        }

    def create_db_connection(self):
        arcpy.CreateDatabaseConnection_management(
            self.__CONNECTION["path"], 
            self.__CONNECTION["name"], 
            self.__CONNECTION["platform"],
            self.__CONNECTION["instance"],
            self.__CONNECTION["auth"],
            self.__CONNECTION["username"],
            self.__CONNECTION["password"],
            self.__CONNECTION["saveUserInfo"],
            self.__CONNECTION["databaseName"],
            self.__CONNECTION["versionName"],
            self.__CONNECTION["saveVersionInfo"])

    def transfer_feature_classes(self):
        db_fcs = arcpy.ListFeatureClasses()
        for fc in db_fcs:
            arcpy.CopyFeatures_management(fc, self.__CONNECTION["path"] + '/' + self.__CONNECTION["name"] + '/' + fc)