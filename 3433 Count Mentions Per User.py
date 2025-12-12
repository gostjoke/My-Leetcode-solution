## 2025/12/12

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        for event, timestamp, message in events:
            if event == "OFFLINE":
                events.append(["ONLINE", str(int(timestamp)+60), message])

        events.sort(key=lambda x:x[0], reverse=True)
        events.sort(key=lambda x: int(x[1]))

        online = set(range(numberOfUsers))

        all_mentioned = 0
        ans = [0] * numberOfUsers

        for event, timestamp, message in events:
            print(event, timestamp, message)
            if event == "MESSAGE":
                if message == "ALL":
                    all_mentioned += 1
                elif message == "HERE":
                    for i in online:
                        ans[i] += 1
                else:
                    for idstr in message.split():
                        ans[int(idstr[2:])] += 1
            elif event == "OFFLINE":
                online.remove(int(message))
            elif event == "ONLINE":
                online.add(int(message))
        for i in range(numberOfUsers):
            ans[i] += all_mentioned

        return ans
