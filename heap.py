def parent(i):
    if i == 0:
        return None
    return (i - 1) // 2


def left(heap, i):
    if i > len(heap):
        return None
    return 2 * i + 1


def right(heap, i):
    if i > len(heap):
        return None
    return 2 * i + 2


def extract_min(heap):
    if not heap:
        return None

    min_elem = heap[0]
    heap[0] = heap.pop()

    i = 0
    while True:
        l = left(i)
        r = right(i)

        smallest = i
        if l < len(heap) and heap[l] < heap[smallest]:
            smallest = l
        if r < len(heap) and heap[r] < heap[smallest]:
            smallest = r

        if smallest != i:
            heap[i], heap[smallest] = heap[smallest], heap[i]
            i = smallest
        else:
            break

    return min_elem


def insert(heap, key):
    heap.append(key)
    i = len(heap) - 1

    while i > 0:
        p = parent(i)
        if p is not None and heap[i] < heap[p]:
            heap[i], heap[p] = heap[p], heap[i]
            i = p
        else:
            break
