HEAD_ADDRESS = 0
TAIL_ADDRESS = 100


class MemoryPool:
    def __init__(self):
        self.memory_address = {}

    def request(self, size):
        head = HEAD_ADDRESS
        if size < 0 or size > TAIL_ADDRESS:
            return 'error'
        if not self.memory_address:
            self.memory_address[HEAD_ADDRESS] = size
        else:
            start_list = sorted(self.memory_address)
            for start in start_list:
                if start - head >= size:
                    self.memory_address[head] = head + size
                else:
                    head = self.memory_address[start]
            if TAIL_ADDRESS - head >= size:
                self.memory_address[head] = head + size
            else:
                return 'error'
        return head

    def release(self, address):
        if self.memory_address.get(address):
            del self.memory_address[address]
        else:
            return 'error'


if __name__ == '__main__':
    memory_pool = MemoryPool()
    while True:
        command = input(">")
        if command.startswith('REQUEST'):
            print(memory_pool.request(int(command.replace('REQUEST=', ''))))
        elif command.startswith('RELEASE'):
            resp = memory_pool.release(int(command.replace('RELEASE=', '')))
            if resp:
                print(resp)
