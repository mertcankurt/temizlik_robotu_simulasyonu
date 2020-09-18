# temizlik_robotu_simulasyonu



Temizlik Robotu Simülasyonu




Workspace yok ise workspace oluşturunuz.

Örn. http://wiki.ros.org/catkin/Tutorials/create_a_workspace

Daha sonra workspace gidiniz ve paketi indiriniz.

cd <WORKSPACE_NAME>/src

git clone "https://github.com/inomuh/temizlik_robotu_simulasyonu.git"

gedit ~/.bashrc

export GAZEBO_MODEL_PATH=~/<WORKSPACE_NAME>/src/temizlik_robotu_simulasyonu/:$GAZEBO_MODEL_PATH

cd <WORKSPACE_NAME>

catkin_make

catkin_make install

source devel/setup.bash

$ roslaunch evarobotmove_gazebo temizlik_robotu_baslat.launch