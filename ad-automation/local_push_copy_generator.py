# -*- coding: utf-8 -*-
"""
抖音本地推投放文案生成器
功能：自动生成团购套餐、POI引流、门店引流文案
"""

def generate_local_push_copy():
    print("=" * 50)
    print("        pop-AI | 本地推投放文案生成器")
    print("=" * 50)
    
    store_name = input("1. 门店名称：")
    business = input("2. 经营品类（餐饮/美业/休闲娱乐等）：")
    package = input("3. 团购套餐名称：")
    discount = input("4. 优惠力度/价格：")
    location = input("5. 门店地址/商圈：")
    
    print("\n【正在生成本地推高转化文案...】\n")
    
    # 生成标题
    print("📌 本地推标题：")
    titles = [
        f"{store_name} | {package} 仅需{discount}！",
        f"{location}必吃！{store_name}{package}太划算",
        f"🔥{store_name}{business}福利！{package}{discount}",
        f"本地人推荐！{store_name}{package}手慢无",
        f"{store_name}开业福利！{package}限时{discount}"
    ]
    for i, t in enumerate(titles, 1):
        print(f"{i}. {t}")
    
    # 生成描述文案
    print("\n📝 团购描述文案：")
    desc = f"""
📍{store_name}
✨{business}人气店
🍱爆款套餐：{package}
💰超值价：{discount}
📍地址：{location}

本地专属福利，点击左下角立即抢购！
到店核销，随时可退！
"""
    print(desc)
    print("✅ 文案生成完成！可直接复制到本地推投放！")

if __name__ == "__main__":
    generate_local_push_copy()
