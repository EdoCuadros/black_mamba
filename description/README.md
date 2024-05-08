# Descripción

En esta carpeta se encuentran los archivos .xacro y las mallas del Roomba y la D435 para las simulaciones.

## Archivo principal

En el archivo principal **robot.urdf.xacro** se incluyen los diferentes archivos para la descripción de la plataforma. Se encuentran archivos para el modelo urdf del robot y de la cámara y para el manejo del robot.

## Descripción del robot. 

Se realiza el modelo urdf del robot, se toma el mallado del Create 2 para el link base y se agregan los sensores. Basado en modelo de [AutonomyLab](https://github.com/AutonomyLab/create_robot/tree/iron/create_description).

## Control para Gazebo

Se realizó un primer control para gazebo que no usa *ros2_control*. Funciona para teleoperación con teclado y mando DualShock4.

Se establecen las juntas de las ruedas, su separación y su diámetro. 

#TODO: Complementar con el funcionamiento del nodo del DS4.

## Controlador con ros2_control

Posteriormente al controlador de ros, se implementó un controlador usando *ros2_control*.  Se fijan los valores máximos y mínimos para la velocidad de cada rueda y se establecen las interfaces. Este archivo está relacionado con my_controllers.

#TODO: Linkear los archivos con enlaces directos.

## Descripción de cámara de profundidad.

Descripción de la cámara RealSense D435, usando controladores de ros. No se ha encontrado la forma de poder usar los paquetes propios de Intel para el uso de la cámara junto con el robot en Gazebo, por lo que no se usaron a partir de ahí.

#TODO: Revisar valores de resolución y profundidad mínima y máxima.

#FIXME: El modelo de la cámara en Gazebo no cuadra con la dirección en la que apunta la imágen. 

