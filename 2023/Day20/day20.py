####### SETUP
with open("day20_input.txt", "r") as file:
    lines = file.readlines()

####### PART 1
class FlipFlop():
    def __init__(self, name, receivers = []):
        self.signal = 0
        self.name = name
        self.receivers = receivers

    def receivePulse(self, name, signal):
        if signal == 0 and self.signal == 0:
            self.signal = 1
            return True
        elif signal == 0 and self.signal == 1:
            self.signal = 0
            return True
        else:
            return False
    
    def sendPulse(self):
        modules = []
        for receiver in self.receivers:
            if self.signal == 1:
                pulse_count["high"] += 1
                if receiver.receivePulse(self.name, 1):
                    modules.append(receiver)
            elif self.signal == 0:
                pulse_count["low"] += 1
                if receiver.receivePulse(self.name, 0):
                    modules.append(receiver)
        return modules
    
    def updateReceivers(self, receivers):
        self.receivers = receivers

class Conjunction():
    def __init__(self, name, inputs = [], receivers = []):
        self.name = name
        self.inputs = {input: 0 for input in inputs}
        self.receivers = receivers

    def receivePulse(self, name, signal):
        self.inputs[name] = signal
        return True
    
    def sendPulse(self):
        modules = []
        if all(self.inputs.values()):
            for receiver in self.receivers:
                pulse_count["low"] += 1
                if receiver.receivePulse(self.name, 0):
                    modules.append(receiver)
        else:
            for receiver in self.receivers:
                pulse_count["high"] += 1
                if receiver.receivePulse(self.name, 1):
                    modules.append(receiver)
        return modules

    def updateReceivers(self, receivers):
        self.receivers = receivers

    def updateInputs(self, inputs):
        self.inputs = {input: 0 for input in inputs}

class Broadcaster():
    def __init__(self, name="Broadcaster", receivers = []):
        self.name = name
        self.receivers = receivers

    def sendPulse(self): # need to split into receivePulse and sendPulse because need to queue them instead of auto triggering the next thing. this would be receivePulse and then return True if trigger to add object to queue (kinda)
        modules = []
        for receiver in self.receivers:
            pulse_count["low"] += 1
            if receiver.receivePulse(self.name, 0):
                modules.append(receiver)
        return modules

    def updateReceivers(self, receivers):
        self.receivers = receivers

class Machine():
    def __init__(self, broadcaster):
        self.broadcaster = broadcaster
        self.module_queue = []

    def push_button(self):
        pulse_count["low"] += 1
        modules = self.broadcaster.sendPulse()
        self.module_queue.extend(modules)

        while self.module_queue:
            module = self.module_queue.pop(0)
            self.module_queue.extend(module.sendPulse())

# instantiate objects
flip_flops = []
conjunctions = []
pulse_count = {"low": 0, "high": 0}
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
    if written_receivers[0] not in [flip_flop.name for flip_flop in flip_flops] and written_receivers[0] not in [conjunction.name for conjunction in conjunctions]:
        load_receivers.append(FlipFlop(written_receivers[0])) # probably a better way to write this and won't work if multiple 'outputs

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

machine = Machine(broadcaster)
print("---")
for _ in range(1000):
    machine.push_button()
print(pulse_count)
print(pulse_count["low"]*pulse_count["high"])

