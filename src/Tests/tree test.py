# Parser test
from anytree import Node, RenderTree, LevelOrderIter


def start():

    action = Node("Initialize", type="Initialize", component="NavigationController")
    task1_navController = Node("sync_navigator", type="Success", parent=action, component="NavigationController")
    task1_success_navController = Node("debug_sync_navigator", type="Error", parent=task1_navController, component="NavigationController")
    task1_error_navController = Node("debug_sync_navigator", type="Error", parent=task1_navController, component="NavigationController")
    task2_error_navController = Node("end_of_task", type="Success", parent=task1_error_navController, component="NavigationController")
    task2_navController = Node("init_sensors", type="Success", parent=task1_success_navController, component="NavigationController")
    task2_error_navController = Node("debug_wheels", type="Error", parent=task1_success_navController, component="NavigationController")

    task1_weedingController = Node("init_camera", type="Success", parent=action, component="WeedingController")
    task1_success_weedingController = Node("init_weeding", type="Success", parent=task1_weedingController, component="WeedingController")
    task1_error_weedingController = Node("debug_camera", type="Error", parent=task1_weedingController, component="WeedingController")
    task2_success_weedingController = Node("end_of_task", type="Success", parent=task1_success_weedingController, component="WeedingController")
    task2_error_weedingController = Node("debug_weeding", type="Error", parent=task1_success_weedingController, component="WeedingController")
    task3_success_weedingController = Node("resume_initialisation", type="Success", parent=task2_error_weedingController, component="WeedingController")


    for pre, fill, node in RenderTree(action):
        print("%s%s" % (pre, node.name))

if __name__ == '__main__':
    start()