# -*- coding: utf-8 -*-
"""
巨量千川投放文案生成器
功能：自动生成投放标题、商品文案、团购文案、高转化描述
"""

def generate_qianchuan_copy():
    print("=" * 50)
    print("        pop-AI | 千川投放文案生成器")
    print("=" * 50)
    
    # 输入信息
    product = input("1. 商品/团购名称：")
    scene = input("2. 使用场景（餐饮/美业/休闲/电商）：")
    advantage = input("3. 核心卖点（最多3个）：")
    price = input("4. 价格/优惠信息：")
    
    print("\n【正在生成千川高转化文案...】\n")
    
    # 生成标题
    print("📌 投放标题（可直接用）：")
    titles = [
        f"【爆款】{product} 限时{price}！",
        f"{scene}必抢！{product} 超划算 {price}",
        f"{advantage}！{product} 仅需{price}",
        f"本地人都在买！{product} {price} 速抢",
        f"🔥{product} 火爆上线！{advantage} {price}"
    ]
    for i, t in enumerate(titles, 1):
        print(f"{i}. {t}")
    
    # 生成文案
    print("\n📝 投放描述文案：")
    desc = f"""
{product}火爆来袭！
✅ 核心优势：{advantage}
✅ 适用场景：{scene}
✅ 超值优惠：{price}

本地专属福利，手慢无！
点击下单，立即享受！
"""
    print(desc)
    
    print("✅ 文案生成完成！可直接复制到千川投放！")

if __name__ == "__main__":
    generate_qianchuan_copy()
