def hanoi_tower(disks=4, source="A", auxiliary="B", target="C"):
    if disks == 1:
        return
    hanoi_tower(disks - 1, source, target, auxiliary)
    hanoi_tower(disks - 1, auxiliary, source, target)
