function [tree] = ID3(data, attributes_aval, sub_attributes, depth_input)
    
    %tree = struct('node','null','left','null','right','null'); wrong
    %because think about number of outputs -> can be 3 or can be 4
    
    %setting depth of the tree
    %parameters 
    global depth;
    global node; 
    global node_storage_array;
    global depth_input;
    
    %tree struct to store nodes and labels
    tree = struct('value', 'null', 'left', 'null', 'right', 'null', 'midright', 'null','midleft','null');
    counter_array = zeros(1,4);
    
    %find number of attributes available for use
    numAttributesAval = 0;
    for i=1:6
        if attributes_aval(i) ~= "-1"
            numAttributesAval = numAttributesAval+1;
        end 
    end 
    
    %returns size of matrix 
    for i=1:size(data,1)
            if(data(i,:,depth)) == "0"
                length1 = i - 1;
                break;
            elseif i == size(data,1)
                length1 = size(data,1);
            end 
    end 
    
    %check and see if we have reached out desired depth
    counter1 = 0;counter2=0;counter3 = 0;counter4 = 0; width = 7;
    if (depth - 1 == depth_input)
        for i=1:length1
            if (data{i,width,depth} == "unacc")
                counter1 = counter1+1;
            elseif (data{i,width,depth} == "acc")
                counter2 = counter2+1;
            elseif (data{i,width,depth} == "good")
                counter3 = counter3+1;
            elseif (data{i,width,depth} == "vgood")
                counter4 = counter4+1;
            end 
        end 
        
        counter_array = [counter1,counter3,counter3,counter4];
        [counter_max,counter_index] = max(counter_array);
        
        if counter_index == 1
            leaf_node = "unacc";
        elseif counter_index == 2
            leaf_node = "acc";
        elseif counter_index == 3
            leaf_node = "good";
        elseif counter_index == 4
            leaf_node = "vgood";
        end 
        
        tree.value = leaf_node;
        
        depth = depth - 1;
        %added this in 
        
        if (node == "buying")
            if (sub_attributes(1:4,1) == "-1")
                depth = depth - 1;
%                 if depth == depth_input - 1
%                     return;
%                 end
                node_available = node_storage_array(depth);
                node_available = return_node_string(node_available);
                attributes_aval = addbackattribute(node_available,attributes_aval);
                
                attributes_aval(1) = "buying";
                sub_attributes(1:4,1) = ["vhigh"; "high"; "med"; "low"];
            else
                attributes_aval(1) = "buying";
            end
        elseif (node == "maint")
            if (sub_attributes(1:4,2) == "-1")
                depth = depth - 1;
%                 if depth == depth_input - 1
%                     return;
%                 end
                node_available = node_storage_array(depth);
                node_available = return_node_string(node_available);
                attributes_aval = addbackattribute(node_available,attributes_aval);
                
                attributes_aval(2) = "maint";
                sub_attributes(1:4,2) = ["vhigh"; "high"; "med"; "low"];
            else
                attributes_aval(2) = "maint";
            end 
        elseif (node == "doors")
            if (sub_attributes(1:4,3) == "-1")
                depth = depth - 1;
%                 if depth == depth_input - 1
%                     return;
%                 end
                node_available = node_storage_array(depth);
                node_available = return_node_string(node_available);
                attributes_aval = addbackattribute(node_available,attributes_aval);
                
                attributes_aval(3) = "doors";
                sub_attributes(1:4,3) = ["2"; "3"; "4"; "more"];
            else
                attributes_aval(3) = "doors";
            end
        elseif (node == "persons")
            if (sub_attributes(1:4,4) == "-1")
                depth = depth - 1;
                if depth == depth_input - 1
                    if sub_attributes(1:4,6) == "-1"
                        return;
                    end 
                end
                node_available = node_storage_array(depth);
                node_available = return_node_string(node_available);
                attributes_aval = addbackattribute(node_available,attributes_aval);
                
                attributes_aval(4) = "persons";
                sub_attributes(1:4,4) = ["2"; "3"; "more";"-1"];
            else
                attributes_aval(4) = "persons";
            end
        elseif (node == "lug_boot")
            if (sub_attributes(1:4,5) == "-1")
                depth = depth - 1;
%                 if depth == depth_input - 1
%                     return;
%                 end
                node_available = node_storage_array(depth);
                node_available = return_node_string(node_available);
                attributes_aval = addbackattribute(node_available,attributes_aval);
                
                attributes_aval(5) = "lug_boot";
                sub_attributes(1:4,5) = ["small"; "med"; "big";"-1"];
            else
                attributes_aval(5) = "lug_boot";
            end
        elseif (node == "safety")
            if (sub_attributes(1:4,6) == "-1")
                depth = depth - 1;
                if depth == depth_input - 1
                    return;
                end
                node_available = node_storage_array(depth);
                node_available = return_node_string(node_available);
                attributes_aval = addbackattribute(node_available,attributes_aval);
                
                attributes_aval(6) = "safety";
                %sub_attributes(1:4,6) = ["low"; "med"; "high";"-1"];
            else
                attributes_aval(6) = "safety";
            end
        end 
    
    %see if the labels are all the same = pure, if so, store the label as
    %leaf node
    elseif all(data(1:length1,7,depth)=="unacc") || all(data(1:length1,7,depth)=="acc") || all(data(1:length1,7,depth)=="vgood") || all(data(1:length1,7,depth)=="good")
        
        if all(data(1:length1,7,depth)=="unacc")
            leaf_node = "unacc";
        elseif all(data(1:length1,7,depth)=="acc")
            leaf_node = "acc";
        elseif all(data(1:length1,7,depth)=="vgood")
            leaf_node = "vgood";
        elseif all(data(1:length1,7,depth)=="good")
            leaf_node = "good";
        end 
        
        tree.value = leaf_node;

        depth = depth-1;
        
        if (node == "buying")
            if (sub_attributes(1:4,1) == "-1")
                node_available = node_storage_array(depth);
                node_available = return_node_string(node_available);
                attributes_aval = addbackattribute(node_available,attributes_aval);
                depth = depth - 1;
                attributes_aval(1) = "buying";
                sub_attributes(1:4,1) = ["vhigh"; "high"; "med"; "low"];
            else
                attributes_aval(1) = "buying";
            end
        elseif (node == "maint")
            if (sub_attributes(1:4,2) == "-1")
                depth = depth - 1;
                node_available = node_storage_array(depth);
                node_available = return_node_string(node_available);
                attributes_aval = addbackattribute(node_available,attributes_aval);
                
                attributes_aval(2) = "maint";
                sub_attributes(1:4,2) = ["vhigh"; "high"; "med"; "low"];
            else
                attributes_aval(2) = "maint";
            end 
        elseif (node == "doors")
            if (sub_attributes(1:4,3) == "-1")
                depth = depth - 1;
                node_available = node_storage_array(depth);
                node_available = return_node_string(node_available);
                attributes_aval = addbackattribute(node_available,attributes_aval);
                
                attributes_aval(3) = "doors";
                sub_attributes(1:4,3) = ["2"; "3"; "4"; "more"];
            else
                attributes_aval(3) = "doors";
            end
        elseif (node == "persons")
            if (sub_attributes(1:4,4) == "-1")
                depth = depth - 1;
                node_available = node_storage_array(depth);
                node_available = return_node_string(node_available);
                attributes_aval = addbackattribute(node_available,attributes_aval);
                
                attributes_aval(4) = "persons";
                sub_attributes(1:4,4) = ["2"; "3"; "more";"-1"];
            else
                attributes_aval(4) = "persons";
            end
        elseif (node == "lug_boot")
            if (sub_attributes(1:4,5) == "-1")
                depth = depth - 1;
                node_available = node_storage_array(depth);
                node_available = return_node_string(node_available);
                attributes_aval = addbackattribute(node_available,attributes_aval);
                
                attributes_aval(5) = "lugboot";
                sub_attributes(1:4,5) = ["small"; "med"; "big";"-1"];
            else
                attributes_aval(5) = "lug_boot";
            end
        elseif (node == "safety")
            if (sub_attributes(1:4,6) == "-1")
                depth = depth - 1;
                node_available = node_storage_array(depth);
                node_available = return_node_string(node_available);
                attributes_aval = addbackattribute(node_available,attributes_aval);
                
                attributes_aval(6) = "safety";
                sub_attributes(1:4,6) = ["low"; "med"; "high";"-1"];
            else
                attributes_aval(6) = "safety";
            end
        end 
        
    end 
    
    %entropy of dataset
    stuff = entropy_DS(data);
    
    %calc entropy for each attribute
    inf_attr = entropy_attribute(data,attributes_aval);
    gain = stuff - inf_attr;
    
    %pull out node that best maximizes gains
    [node,node_placement] = return_node(gain,attributes_aval);
    tree.value = node;
    node_storage_array(depth) = node_placement;
    attributes_aval(node_placement) = "-1"; 
    
    %pull out sub attribute
    i = 1;
    while(i<5)
        if (sub_attributes(i,node_placement) == "-1")
            if i==4
                depth = depth - 1;
                node_available = node_storage_array(depth);
                node_available = return_node_string(node_available);
                attributes_aval = addbackattribute(node_available,attributes_aval);
                sub_attributes = addbacksubattribute(node_available,sub_attributes);
                if depth == 0
                    if node_available == "safety"
                        return;
                    end 
                end 
                placeholder = node_storage_array(depth);
                node = return_node_string(placeholder);
                node_placement = placeholder;
                i = 0;
            end 
            i=i+1;
        else 
            sub_attribute = sub_attributes(i,node_placement);
            sub_attributes(i,node_placement) = "-1";
            i=5;
        end 
    end 
    
    
    %pull out new dataset
    data = return_subtable(data,node,sub_attribute);
    depth = depth+1;
    
    %call ID3 for new dataset and available attributes
    ID3(data,attributes_aval,sub_attributes);
    
    return; 
end 
