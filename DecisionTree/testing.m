%Testing function
clc;clear all;

T = readtable('train.csv','Format','%s%s%s%s%s%s%s');
data(:,:,1) = string(T{:,:});
attributes_aval = {'buying','maint','doors','persons','lug_boot',"safety"};
attributes_aval = string(attributes_aval);
global depth;
global depth_input
depth = 1;
global node_storage_array;
sub_attribute_counter = 1;
sub_attributes = ["vhigh" "vhigh" "2" "2" "small" "low";"high" "high" "3" "4" "med" "med";"med" "med" "4" "more" "big" "high";"low" "low" "5more" "-1" "-1" "-1"];

prompt = "Enter desired tree depth: ";
depth_input = input(prompt);

ID3(data, attributes_aval, sub_attributes,depth_input)


%done, remove sub_attribute counter from funcitons etc