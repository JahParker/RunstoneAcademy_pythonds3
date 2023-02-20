class LogicGate:
    def __init__(self, label) -> None:
        self.label = label
        self.output = None
    
    def get_label(self):
        return self.label
    
    def get_output(self):
        self.output = self.perform_gate_logic()

        return self.output

class BinaryGate(LogicGate): # A logic Gate that can take two values
    def __init__(self, label) -> None:
        super().__init__(label)
        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        if self.pin_a == None:
            return int(input(f"Enter pin A input for gate {self.get_label()}: "))
        else:
            return self.pin_a.get_from().get_output()
    
    def get_pin_b(self):
        if self.pin_b == None:
            return int(input(f"Enter pin B input for gate {self.get_label()}: "))
        else:
            return self.pin_b.get_from().get_output()

    # Sets pin a and b to the gate being connected to that node
    def set_next_pin(self, source):
        if self.pin_a == None:
            self.pin_a = source
        else:
            if self.pin_b == None:
                self.pin_b = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")

class AndGate(BinaryGate): # A binary gate where two values must be the same value in order to be True
    def __init__(self, label) -> None:
        super().__init__(label)

    def perform_gate_logic(self): # Tests to see if both pins are 1
        a = self.get_pin_a()
        b = self.get_pin_b()
        
        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate): # A binary gate where one value must be True in order to be True
    def __init__(self, label) -> None:
        super().__init__(label)
    
    def perform_gate_logic(self): # Tests to see if either pin is 1
        a = self.get_pin_a()
        b = self.get_pin_b()

        if a == 1 or b == 1:
            return 1
        else:
            return 0
            
"""
class NandGate(BinaryGate): # A binary gate where two values must be the same value in order to be True
    def __init__(self, label) -> None:
        super().__init__(label)

    def perform_gate_logic(self): # Tests to see if both pins are 1
        a = self.get_pin_a()
        b = self.get_pin_b()
        
        if a == 1 and b == 1:
            return int(not 1)
        else:
            return int(not 0)
"""
class NandGate(AndGate): # A simpler way to do the above
    def perform_gate_logic(self):
        if super().perform_gate_logic() == 1:
            return 0
        else:
            return 1


"""
class NorGate(BinaryGate): # A binary gate where one value must be True in order to be True
    def __init__(self, label) -> None:
        super().__init__(label)
    
    def perform_gate_logic(self): # Tests to see if either pin is 1
        a = self.get_pin_a()
        b = self.get_pin_b()

        if a == 1 or b == 1:
            return int(not 1)
        else:
            return int(not 0)
"""
class NorGate(OrGate): # A simpler way to do the above
    def perform_gate_logic(self):
        if super().perform_gate_logic() == 1:
            return 0
        else:
            return 1
    

class UnaryGate(LogicGate): # A logic gate that accepts only one value
    def __init__(self, label) -> None:
        super().__init__(label)
        self.pin = None

    def get_pin(self):
        if self.pin == None:
            return int(input("Enter pin input for gate " + self.get_label() + ": "))
        else:
            return self.pin.get_from().get_output()

    def set_next_pin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")

class NotGate(UnaryGate): # A unary gate that returns the opposite value
    def __init__(self, label) -> None:
        super().__init__(label)

    def perform_gate_logic(self): # Returns the opposite pin value
        pin = self.get_pin()

        
        if pin == 1:
            return 0
        else:
            return 1

class Connector:
    def __init__(self, f_gate, t_gate) -> None:
        self.from_gate = f_gate
        self.to_gate = t_gate

        t_gate.set_next_pin(self) # The argument is the current logic gate object aka the 'source' parameter in set_next_pin

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate

# g1 = AndGate("G1")
# g2 = AndGate("G2")
# g3 = OrGate("G3")
# g4 = NotGate("G4")
# c1 = Connector(g1, g3)
# c2 = Connector(g2, g3)
# c3 = Connector(g3, g4)
# print(g4.get_output())

nag2 = NandGate('NAG2')
nag1 = NandGate('NAG1')
nog1 = NorGate('NOG1')
c1 = Connector(nag1, nog1)
c1 = Connector(nag2, nog1)
print(nog1.get_output())


nag1 = NandGate('NAG1')
nag2 = NandGate('NAG2')
ag1 = NorGate('AG1')
c1 = Connector(nag1, ag1)
c1 = Connector(nag2, ag1)
print(nog1.get_output())