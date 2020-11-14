/*
 Navicat Premium Data Transfer

 Source Server         : mysql80
 Source Server Type    : MySQL
 Source Server Version : 80019
 Source Host           : localhost:3306
 Source Schema         : test_py

 Target Server Type    : MySQL
 Target Server Version : 80019
 File Encoding         : 65001

 Date: 26/09/2020 09:48:04
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for index_comment
-- ----------------------------
DROP TABLE IF EXISTS `index_comment`;
CREATE TABLE `index_comment`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `comment_text` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `stars` tinyint(0) NOT NULL,
  `time_log` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of index_comment
-- ----------------------------
INSERT INTO `index_comment` VALUES (1, '杀手', 2, '2020-05-05');
INSERT INTO `index_comment` VALUES (2, '好看！全程无尿点。熊孩子坑爹的故事，这部电影告诉我们——子女教育太重要了，至少要知道什么人不能惹。拍得很二次元，基努里维斯大叔帅到没边，拳拳到肉的感觉看着很过瘾', 5, '2014-10-31');
INSERT INTO `index_comment` VALUES (3, '惊喜。足够简单粗暴：在这个片子里台词多的人物都被杀了；男主逻辑是「你杀我狗，偷我车，我灭你全家」；报仇时都不等仇家一句话说完就结果了对方，没一句逼逼。另外基努瘦了穿西装真好看。', 4, '2014-10-25');
INSERT INTO `index_comment` VALUES (4, '又名“你杀我爱狗，我宰你全家”，画个讽刺漫画会送命，杀条狗会死人，本片引进给国内爱狗人士看，估计大热，不过应改名《别惹爱狗族》。最近美国杀手都和俄罗斯黑帮杠上了，本片可以和丹泽尔·华盛顿的新片《伸冤人》一起观赏，', 4, '2014-01-14');
INSERT INTO `index_comment` VALUES (5, '被影评骗了 我觉得动作并不是很出彩 看得出来很多动作像是自己完成的 所以才觉得看上去有点笨笨呆呆慢慢的... 算比较紧凑的复仇片 但没有什么记忆深刻的地方 看完觉得wick这个人物也不过是主角光环~', 3, '2014-11-02');
INSERT INTO `index_comment` VALUES (6, '基努里维斯终于帅回来了。前半个小时告诉观众，这些人惹到神了，马上要挂；后七十分钟就看他们怎么挂掉。 Android\r\n\r\n', 3, '2015-01-14');
INSERT INTO `index_comment` VALUES (7, '小狗狗那么可爱！怎么可以杀小狗狗！干你们黑社会的娘辣！', 4, '2017-08-24');
INSERT INTO `index_comment` VALUES (8, '对于我来说全片最高潮的一幕是地下室黑版康斯坦丁附体那两枪，热泪盈眶。不变的发际线，不变的身材，不变的O型腿内八字，不变的男神，才是真的男神。收尸小分队的头头是Da。杀手隐藏世界观设置超带感，+HE。', 5, '2014-11-07');
INSERT INTO `index_comment` VALUES (9, '干净利落 Android', 4, ' 2015-02-06');
INSERT INTO `index_comment` VALUES (10, '你要我的“狗命”，我就要你的狗命。', 3, ' 2017-05-10');
INSERT INTO `index_comment` VALUES (11, '俩专业特技演员带着一专业面瘫和专业大佬专业二世祖专业酱油一起搞了一出超长十八禁MV。Alfie一如既往让人想抽丫两巴掌，全片一直操着不标【piao】准的罗刹口音在重复，大哥就为了一条狗吗，就为了一条狗啊大哥！歌单得点二十个赞，【减肥后的】基努杀人杀得干脆利落，可惜编剧智商全程掉线', 4, '2014-11-04');
INSERT INTO `index_comment` VALUES (12, '一条狗引发的血案。', 3, '2017-02-01');
INSERT INTO `index_comment` VALUES (13, '简单！粗暴！任性！花痴！咋地！', 4, '2015-01-29');
INSERT INTO `index_comment` VALUES (14, '这应该是铁血直男款小时代没有错了，你们看这设定：不洗头也帅破表的世界最强杀手，完美的老婆漂亮的房子悲情的故事背景，巨又钱却有个傻逼儿子的黑帮老大，住满杀手的豪华酒店，拿杀手金币当通行证。这不是意淫是啥嘛！剧情漏洞大过天都不想说了，但是基努套上西装演啥我都爱看，咋的咯', 3, ' 2017-03-28');
INSERT INTO `index_comment` VALUES (15, '基诺没老，还能再战三十年', 4, ' 2015-01-14');
INSERT INTO `index_comment` VALUES (16, '非常有逼格的杀手片 iPhone', 4, '2015-01-14');
INSERT INTO `index_comment` VALUES (17, '剧情很蠢，但动作枪战戏拍得不错，漫画式的酷劲和幽默感特别加分。《权力的游戏》又贡献一个被“定型”的演员，看来阿尔菲·艾伦以后只能演席恩·格雷乔伊式的角色了。', 3, '2014-11-03');
INSERT INTO `index_comment` VALUES (18, '打狗不看主人的从来都是不知道死字怎么写的主，古今中外概莫能外。我就知道是在纯飙肾上腺素……', 3, ' 2015-02-02');
INSERT INTO `index_comment` VALUES (19, '以后对于这种火爆枪战片全部满分好么？还有丧妻独居，连只狗都被人队咗，这样自虐的剧本都上阵，里维斯叔叔真心坚强', 5, '2015-01-14');
INSERT INTO `index_comment` VALUES (20, '三星半，铁血复仇之战，前奏稍有些快，基石没打好，随后便是简单粗暴的屠杀大戏，基努减肥成功，杀人从不废话，KO+爆头一气呵成，非常爽快，有意思的是营造了一个充满秩序的地下世界，杀手酒店的设定很棒，几位老戏骨出场不多但很有韵味。', 4, '2015-01-19');
INSERT INTO `index_comment` VALUES (21, '最爱看纯爷们为女儿/媳妇/父母/猫狗将暴徒花样轰杀至渣的类型了！基努瘦身成功后演了一个连姆叔叔的角色，然而击杀量却是后者的十几倍，而且这种枪斗术技法，比撕裂的末日还带感啊！', 4, '2015-01-16');
INSERT INTO `index_comment` VALUES (22, '约翰·威客又名【别惹狗奴】，这样的戏剧冲突设定就儿戏般让人难以直视，它剩下的任务就是让一个面瘫帅大叔干掉百十号人，端掉整个俄罗斯黑帮，卡通化的暴力谈不上酷炫，也谈不上热血和爽，毕竟我们不用担心超人一般的前救世主会中途挂掉，他是男主角，用脚趾头想也知道他会神功附体。★★', 2, '2015-01-15');
INSERT INTO `index_comment` VALUES (23, '对于这种片，我一般只有一个要求，就是不要犯明知对方厉害逮着了还不直接杀掉这样最低级的错误。可惜的是，就这么低级的错误，总有人再三犯', 2, '2015-02-03');

SET FOREIGN_KEY_CHECKS = 1;
