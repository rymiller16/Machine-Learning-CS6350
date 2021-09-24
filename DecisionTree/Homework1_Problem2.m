%Ryan Miller
%u1067596
%Machine Learning 
%Homework 1

T = readtable('train.csv','Format','%s%s%s%s%s%s%s');
data(:,:,1) = string(T{:,:});
attributes_aval = {'buying','maint','doors','persons','lug_boot',"safety"};
attributes_aval = string(attributes_aval);
global depth;
global sub_attribute_counter;
depth = 0;
sub_attribute_counter = 1;

a = ["stuff stuff" "no such thing"];
if (a(1,1) == "stuff stuff")
    disp("yes")
end 

%buying, maint, doors, persons, lug boot, safety
sub_attributes = ["vhigh" "vhigh" "2" "2" "small" "low";"high" "high" "3" "4" "med" "med";"med" "med" "4" "more" "big" "high";"low" "low" "5more" "-1" "-1" "-1"];


%entropy calc for data
stuff = entropy_DS(data);

%calc entropy for each attribute
inf_attr = entropy_attribute(data,attributes_aval);
gain = stuff - inf_attr;

%pull out first node
[node,node_placement] = return_node(gain,attributes_aval);
attributes_aval(node_placement) = "-1";
depth = depth+1;

sub_attribute = sub_attributes(sub_attribute_counter,node_placement);
%now need to split data to follow path
data = return_subtable(data,node,sub_attribute);
stuff = entropy_DS(data);
inf_attr = entropy_attribute(data,attributes_aval);
gain = stuff - inf_attr;

%with new data, need to calculate entropy and pick another node






%note A(2,4) = row 2 column 4





        