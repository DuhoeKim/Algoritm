def solution(bridge_length, weight, truck_weights):
    time = 0
    on_bridge = [0] * bridge_length
    truck_weights = truck_weights[::-1]
    now_weight = 0

    while truck_weights:
        time += 1
        now_weight -= on_bridge.pop(0)

        if now_weight + truck_weights[-1] <= weight:
            now_weight += truck_weights[-1]
            on_bridge.append(truck_weights.pop())
        else:
            on_bridge.append(0)

    time += bridge_length
    return time