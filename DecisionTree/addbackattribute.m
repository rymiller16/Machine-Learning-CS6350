function attributes_aval = addbackattribute(node_string,attributes_aval)
    if node_string == "buying"
        attributes_aval(1) = "buying";
    elseif node_string == "maint"
        attributes_aval(2) = "maint";
    elseif node_string == "doors"
        attributes_aval(3) = "doors";
    elseif node_string == "persons"
        attributes_aval(4) = "persons";
    elseif node_string == "lug_boot"
        attributes_aval(5) = "lug_boot";
    elseif node_string == "safety"
        attributes_aval(6) = "safety";
    end
end