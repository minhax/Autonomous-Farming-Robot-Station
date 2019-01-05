# Parser test
from IA_Serveur.src.Mapping.Mapping import *
from Parser.parser import *
from anytree import Node, RenderTree, LevelOrderIter
from anytree.exporter import DotExporter
def start():
    action = Node("Initialize", type="Initialize")
    task1_navController = Node("sync_navigator", type="Success", parent=action)
    task1_success_navController = Node("debug_sync_navigator", type="Error", parent=task1_navController)
    task1_error_navController = Node("debug_sync_navigator", type="Error", parent=task1_navController)
    task2_error_navController = Node("end_of_task", type="Success", parent=task1_error_navController)
    task2_navController = Node("init_sensors", type="Success", parent=task1_success_navController)
    task2_error_navController = Node("debug_wheels", type="Error", parent=task1_success_navController)

    task1_weedingController = Node("init_camera", type="Success", parent=action)
    task1_success_weedingController = Node("init_weeding", type="Success", parent=task1_weedingController)
    task1_error_weedingController = Node("debug_camera", type="Error", parent=task1_weedingController)
    task2_success_weedingController = Node("end_of_task", type="Success", parent=task1_success_weedingController)
    task2_error_weedingController = Node("debug_weeding", type="Error", parent=task1_success_weedingController)
    task3_success_weedingController = Node("resume_initialisation", type="Success", parent=task2_error_weedingController)




    for pre, fill, node in RenderTree(action):
        print("%s%s" % (pre, node.name))

if __name__ == '__main__':
    start()