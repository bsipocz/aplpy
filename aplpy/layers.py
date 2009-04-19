class Layers(object):
    
    def __init__(self):
        pass
    
    def _initialize_layers(self):
        
        self._layers_list = []
        self._contour_counter = 0
        self._scatter_counter = 0
    
    def list_layers(self):
        
        n_layers = len(self._layers_list)
        if n_layers == 0:
            print "\n  There are no layers in this figure"
        else:
            if n_layers==1:
                print "\n  There is one layer in this figure:\n"
            else:
                print "\n  There are "+str(n_layers)+" layers in this figure:\n"
            for layer in self._layers_list:
                if layer['visible']:
                    print "   -> "+layer['name']
                else:
                    print "   -> "+layer['name']+" (hidden)"
    
    def layer_exists(self,layer):
        for l in self._layers_list:
            if layer==l['name']:
                return True
        return False
    
    def _name_empty_layers(self,name):
        
        empty = []
        for i in range(len(self._ax1.collections)):
            try:
                n = self._ax1.collections[i].aplpy_layer_name
            except AttributeError:
                empty.append(i)
        
        for i in empty:
            self._ax1.collections[i].aplpy_layer_name = name
        
        if len(empty) > 0:
            self._layers_list.append({'name' : name,'visible' : True})
    
    def remove_layer(self,layer,raise_exception=True):
        
        if not self.layer_exists(layer):
            if raise_exception:
                raise Exception("Layer "+layer+" does not exist")
            return
        
#        if "contour_set_" in layer or "scatter_set_" in layer:
        for i in range(len(self._ax1.collections)-1,-1,-1):
            if(layer==self._ax1.collections[i].aplpy_layer_name):
                self._ax1.collections.pop(i)
        
        for i in range(len(self._layers_list)-1,-1,-1):
            if self._layers_list[i]['name']==layer:
                self._layers_list.pop(i)
        
        self.refresh()
    
    def hide_layer(self,layer,raise_exception=True):
        
        if not self.layer_exists(layer):
            if raise_exception:
                raise Exception("Layer "+layer+" does not exist")
            return
                
#        if "contour_set_" in layer or "scatter_set_" in layer:
        for i in range(len(self._ax1.collections)-1,-1,-1):
            if(layer==self._ax1.collections[i].aplpy_layer_name):
                self._ax1.collections[i].set_visible(False)
        
        for i in range(len(self._layers_list)-1,-1,-1):
            if self._layers_list[i]['name']==layer:
                self._layers_list[i]['visible']=False
        
        self.refresh()
    
    
    def show_layer(self,layer,raise_exception=True):
        
        if not self.layer_exists(layer):
            if raise_exception:
                raise Exception("Layer "+layer+" does not exist")
            return
        
#        if "contour_set_" in layer or "scatter_set_" in layer:
        for i in range(len(self._ax1.collections)-1,-1,-1):
            if(layer==self._ax1.collections[i].aplpy_layer_name):
                self._ax1.collections[i].set_visible(True)
        
        for i in range(len(self._layers_list)-1,-1,-1):
            if self._layers_list[i]['name']==layer:
                self._layers_list[i]['visible']=True
        
        self.refresh()
