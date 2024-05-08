## Launch Files

En esta carpeta se encuentran todos los archivos launch usados para simulaciones y teleoperación con mando DS4.

## Launch sim

Este archivo primero lanza la descripción del robot. 

#TODO: Agregar comando que se usaría para descripción.

Adicionalmente se lanza el simulador Gazebo, generando la entidad del robot. Finalmente inicia los controladores para el manejo diferencial de la plataforma que publican en el tópico */cmd_vel*.

Para el manejo por teclado es necesario correr el paquete de teleoperación de ros.

` ros2 run teleop_twist_keyboard teleop_twist_keyboard`

#TODO: Agregar remapeo.

Es necesario remapear, debido a que normalmente el paquete publica en el tópico */cmd_vel*, sin embargo, el controlador de *ros2_control* esta suscrito al tópico */cmd_vel_unstamped*.

## Joystick launch

De igual forma, este archivo lanza los nodos para el manejo del robot por mando DS4 conectado por cable. Los parámetros de control se toman del archivo *joystick.yaml*. Luego de ejecutar la descripción del robot, se usa el siguiente comando.

`ros2 run black_mamba joystick.launch.py`


