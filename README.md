自用配置

## ACL4SSR_Online_Full_Mannix.ini

自定义 订阅转换 配置转换 规则转换 的远程配置：

https://raw.githubusercontent.com/Alexecz/ACL4SSR/main/ACL4SSR_Online_Full_Mannix.ini


## ACL4SSR_Online_Mannix.ini

去除国家/地区：

https://raw.githubusercontent.com/Alexecz/ACL4SSR/main/ACL4SSR_Online_Mannix.ini


---

⚠ 重要！每个组名的**空格**后面都添加了一个**隐藏字符 \u200d** 用于防止与节点重名，改名需谨慎

移除
- 📢 谷歌FCM
- Ⓜ️ 微软云盘
- Ⓜ️ 微软服务
- 🍎 苹果服务
- 📲 电报消息
- 🎶 网易音乐
- 🎮 游戏平台
- 📹 油管视频
- 🎥 奈飞视频
- 🌏 国内媒体
- 🌍 国外媒体
- 📺 巴哈姆特
- 🇰🇷 韩国节点

重命名
- 🚀 节点选择 -> ✈️ 起飞
- 🚀 手动切换 -> 👆🏻 指定
- ♻️ 自动选择 -> ⚡ 低延迟
- 📺 哔哩哔哩 -> 📺 B站
- 🎯 全球直连 -> 🛩️ 墙内
- 🐟 漏网之鱼 -> 🌐 未知站点
- 🇭🇰 香港节点 -> 🇭🇰 香港
- 🇨🇳 台湾节点 -> 🇹🇼 台湾
- 🇸🇬 狮城节点 -> 🇸🇬 新加坡
- 🇯🇵 日本节点 -> 🇯🇵 日本
- 🇺🇲 美国节点 -> 🇺🇸 美国

合并
- 🛑 广告拦截 + 🍃 应用净化 -> 💩 广告

新增
- 🇨🇳 中国 (含 🇭🇰 香港 🇹🇼 台湾)
- 🎏 其他
- 🤖 ‍AI

url-test
<!-- - 延迟测试链接 http://www.gstatic.com/generate_204 -> https://i.ytimg.com/generate_204 -->
- 间隔时间 300秒 -> 15/30秒
- 容差 50/150毫秒 -> 100/300毫秒

正则匹配大小写、简繁体，更好地匹配中转、IPLC节点

LocalAreaNetwork.list 使用 DIRECT