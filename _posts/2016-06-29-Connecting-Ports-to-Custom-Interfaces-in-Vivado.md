---
layout: post
title: "Connecting Ports to Custom Interfaces in Vivado"
date: 2016-06-29 20:15:19
---
When first starting work with custom IP in Xilinx, it can be difficult to connect custom interfaces to ports. Interface ports don't follow the same rules as normal buses in Vivado, so this page is a guide to a variety of common mishaps. 

<img src="https://github.com/wanderso/wanderso.github.io/blob/master/blog/images/2016-06-15_problem_in_block_design.png" border="0" alt="The problem." style="max-width:100%"/>
![The problem.](https://github.com/wanderso/wanderso.github.io/blob/master/blog/images/2016-06-15_problem_in_block_design.png){:style="max-width:100%;"}

For this example post, we'll be using the [Arty Artix-7 FPGA Development Board](http://www.digikey.com/catalog/en/partgroup/arty-artix-7-fpga-development-board/57656?WT.srch=1&gclid=CJzEjPqVrc0CFcdhfgodGH8IQA) with the [Organic-LED RGB](http://store.digilentinc.com/pmodoledrgb-96-x-64-rgb-oled-display-with-16-bit-color-resolution/) *P*eripheral *Mod*ule.

![Pmod from Digilent with pin missing](https://github.com/wanderso/wanderso.github.io/blob/master/blog/images/2016-06-15_no_pin.png)

First, in order to use custom IP at all, you need to add the IP. For the Arty and the PMods, this can be found [on Digilent's github page](https://github.com/Digilent/vivado-library). Download and unpack the libraries to the directory of your choice. Then add them to your project; look for the Flow Navigator (by default on the left border of Vivado's default view) and click Project Settings. In the ensuing popup, click "IP", and then switch to the Repository Manager tag.

![The window should look like this](https://github.com/wanderso/wanderso.github.io/blob/master/blog/images/2016-06-17_Navigation_guide.png)

Once you have opened the repository manager, navigate to the directory. Once youv've navigated there, open up the root directory for the download. You should see /ip and /if subfolders in your selection.

![Make sure that the vivado-library-master folder is selected, not the /ip or /if folder](https://github.com/wanderso/wanderso.github.io/blob/master/blog/images/2016-06-17_if_ip_subdir.png)

When you add the folder to your repository, the following window should pop up, indicating that both IP *and* interfaces have been successfully added to your repository. 

![If either of these two numbers are zero, problems will develop](https://github.com/wanderso/wanderso.github.io/blob/master/blog/images/2016-06-15_vivado_library_IPs_and_interfaces.png)

Once you've verified that there are both IPs and Interfaces in the desired folder, you can add the folder by default to all new projects. Go to the Tools menu at the top of the Vivado window, and select Options from the bottom of the Tools menu. This should bring you to the Vivado Options screen, where the first option under General should be to set up the default user-created repositories. 

![Once this list is changed, all new projects will include the by default.](https://github.com/wanderso/wanderso.github.io/blob/master/blog/images/2016-06-18_Vivado_Default_IP_Repo.png)

Now that the repositories have been added, they can be viewed in the Vivado IP catalog, also selectable under the Project Manager in the Flow Navigator. The folders can be opened to view details about what IP has been added.

![The library](https://github.com/wanderso/wanderso.github.io/blob/master/blog/images/2016-06-18_Vivado_IP_Library_Open.png)

Once the IP is functional, it needs to be connected to your board. Switch to the board view. There should be an 'Add IP' button - a chip with a '+' symbol on it. 

![Add IP button is here](https://github.com/wanderso/wanderso.github.io/blob/master/blog/images/2016-06-18_Add_IP.png)

Then, use the search bar to find your custom device. 

![PMod](https://github.com/wanderso/wanderso.github.io/blob/master/blog/images/2016-06-18_Add_PMOD.png)

Once the device has been added to the board, the interface is needed for the PMod to communicate with the rest of the board. Note the + and the \|\|\| on the device's right edge. This indicates that a special 'interface port' is used here, and not a standard wire or bus. 

![PMod](https://github.com/wanderso/wanderso.github.io/blob/master/blog/images/2016-06-15_no_pin.png)

When using the Arty and a PMod for this demonstration, plug the PMod into the connector of your choice. Then, select the 'board' view on the Sources//Design//Signals//Board pane just below the block design. Scroll down to the section listing the PMod connectors on the board, then click and drag the connector you selected to the +\|\|\| pin on the IP block. If you have the custom IP and the Interfaces both installed, this will connect the interface to the port, creating a new pin for Vivado to use.

![After the pin is connected](https://github.com/wanderso/wanderso.github.io/blob/master/blog/images/20160615_when_pin_connected.png)

If the interfaces are not properly installed, errors will result. "Could not find bus definition for the interface", "Could not find abstraction definition for the interface", and "Arguments to the connect_bd_intf_net command cannot be empty" are the three most common.

![This message comes up when attempting to connect interface](https://github.com/wanderso/wanderso.github.io/blob/master/blog/images/2016-06-15_problem_in_block_design.png) 
![This message comes up while trying to run Auto Connect](https://github.com/wanderso/wanderso.github.io/blob/master/blog/images/2016-06-15_connect_db_intf_net.png)

If you encounter these errors, double-check the User Repository Manager.

