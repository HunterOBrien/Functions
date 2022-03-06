def calc_gst(net_price):
    return net_price * 1.15


# Main
net_price_ = int(input("Enter price here: "))
print(f"${calc_gst(net_price_):.2f}")
