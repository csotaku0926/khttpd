#!/usr/bin/env python3
from bcc import BPF

code = """
#include <uapi/linux/ptrace.h>

BPF_HASH(start, u64);

int BPF_kprobe(struct pt_regs *ctx)
{
	u64 ts = bpf_ktime_get_ns();
	bpf_trace_printk("in %llu\\n",ts);
	return 0;
}

int BPF_kretprobe(struct pt_regs *ctx)
{
	u64 ts = bpf_ktime_get_ns();
	bpf_trace_printk("out %llu\\n",ts);
	return 0;
}
"""

b = BPF(text=code)
b.attach_kprobe(event="my_kthread_wrapper", fn_name="BPF_kprobe")
b.attach_kretprobe(event="my_kthread_wrapper", fn_name="BPF_kretprobe")

while True:
	res = b.trace_fields()
	print(res[5].decode())