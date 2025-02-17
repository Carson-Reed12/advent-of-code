####### SETUP
with open("day20_input.txt", "r") as file:
    lines = file.readlines()

####### PART 1
class FlipFlop():
    def __init__(self, name, receivers = []):
        self.signal = 0
        self.name = name
        self.receivers = receivers

    def trigger(self, name, signal): # need to split into receivePulse and sendPulse because need to queue them instead of auto triggering the next thing. this would be receivePulse and then return True if trigger to add object to queue
        if signal == 0 and self.signal == 0:
            self.signal = 1
            for receiver in self.receivers:
                receiver.trigger(self.name, 1)
        elif signal == 0 and self.signal == 1:
            self.signal = 0
    
    def updateReceivers(self, receivers):
        self.receivers = receivers

class Conjunction():
    def __init__(self, name, inputs = [], receivers = []):
        self.name = name
        self.inputs = {input: 0 for input in inputs}
        self.receivers = receivers

    def trigger(self, name, signal): # need to split into receivePulse and sendPulse because need to queue them instead of auto triggering the next thing. this would be receivePulse and then return True if trigger to add object to queue
        self.inputs[name] = signal

        if all(self.inputs.values()):
            for receiver in self.receivers:
                receiver.trigger(self.name, 0)
        else:
            for receiver in self.receivers:
                receiver.trigger(self.name, 1)

    def updateReceivers(self, receivers):
        self.receivers = receivers

    def updateInputs(self, inputs):
        self.inputs = {input: 0 for input in inputs}

class Broadcaster():
    def __init__(self, name="Broadcaster", receivers = []):
        self.name = name
        self.receivers = receivers

    def push_button(self): # need to split into receivePulse and sendPulse because need to queue them instead of auto triggering the next thing. this would be receivePulse and then return True if trigger to add object to queue (kinda)
        for receiver in self.receivers:
            receiver.trigger(self.name, 0)

    def updateReceivers(self, receivers):
        self.receivers = receivers

# instantiate objects
flip_flops = []
conjunctions = []
for line in lines:
    if "broadcaster" in line:
        broadcaster = Broadcaster()
    elif "%" in line:
        flip_flops.append(FlipFlop(line.split(" -> ")[0][1:]))
    elif "&" in line:
        conjunctions.append(Conjunction(line.split(" -> ")[0][1:]))

# load connections
for line in lines:
    load_receivers = []
    written_receivers = line.strip().split(" -> ")[1].split(", ")

    for flip_flop in flip_flops:
        if flip_flop.name in written_receivers:
            load_receivers.append(flip_flop)

    for conjunction in conjunctions:
        if conjunction.name in written_receivers:
            load_receivers.append(conjunction)

    if "broadcaster" in line:
        broadcaster.updateReceivers(load_receivers)
    elif "%" in line:
        name = line.split(" -> ")[0][1:]
        [flip_flop for flip_flop in flip_flops if flip_flop.name == name][0].updateReceivers(load_receivers)
    elif "&" in line:
        name = line.split(" -> ")[0][1:]
        [conjunction for conjunction in conjunctions if conjunction.name == name][0].updateReceivers(load_receivers)

for conjunction in conjunctions:
    inputs = []
    for line in lines:
        name = line.split(" -> ")[0][1:]
        receivers = line.strip().split(" -> ")[1].split(", ")
        if conjunction.name in receivers:
            inputs.append(name)
    conjunction.updateInputs(inputs)

print([receiver.name for receiver in broadcaster.receivers])
for flip_flop in flip_flops:
    print(f"{flip_flop.name} - {[receiver.name for receiver in flip_flop.receivers]}")
for conjunction in conjunctions:
    print(f"{conjunction.name} - {[input_name for input_name in conjunction.inputs]} - {[receiver.name for receiver in conjunction.receivers]}")