from anytree import Node

SERVER_URL = "192.168.14.1:8080/mapping.html"
SERVER_IP_ADDRESS = "192.168.14.1"
SERVER_DEFAULT_PORT = 1111
CLIENT_DEFAULT_PORT = 1112

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
