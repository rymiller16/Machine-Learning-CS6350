function [node,I] = return_node(gain,attributes_aval)
    
    for i = 1:6
        if attributes_aval(i) == "-1"
            gain(i) = -1;
        end 
    end 
    
    [M,I] = max(gain);
    node = attributes_aval(I);
end