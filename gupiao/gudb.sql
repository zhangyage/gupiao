/*
Navicat MySQL Data Transfer

Source Server         : mytest
Source Server Version : 50634
Source Host           : 47.94.188.237:3306
Source Database       : gudb

Target Server Type    : MYSQL
Target Server Version : 50634
File Encoding         : 65001

Date: 2018-01-29 16:42:08
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for gu_conctol
-- ----------------------------
DROP TABLE IF EXISTS `gu_conctol`;
CREATE TABLE `gu_conctol` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `gu_name` varchar(255) DEFAULT NULL,
  `gu_num` int(6) unsigned zerofill DEFAULT NULL,
  `link` varchar(255) DEFAULT NULL,
  `yuzhi_up` double(10,3) DEFAULT NULL,
  `yuzhi_down` double(10,3) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of gu_conctol
-- ----------------------------
INSERT INTO `gu_conctol` VALUES ('1', '振华股份', '603067', 'http://hq.sinajs.cn/list=sh603067', '19.770', '19.200');
INSERT INTO `gu_conctol` VALUES ('2', '京能置业', '600791', 'http://hq.sinajs.cn/list=sh600791', '11.800', '11.240');
INSERT INTO `gu_conctol` VALUES ('3', '至纯科技', '603690', 'http://hq.sinajs.cn/list=sh603690', '20.010', '22.020');
INSERT INTO `gu_conctol` VALUES ('4', '宝钛股份', '600456', 'http://hq.sinajs.cn/list=sh600456', '28.000', '26.000');
INSERT INTO `gu_conctol` VALUES ('5', '西部建设', '002302', 'http://hq.sinajs.cn/list=sz002302', '19.250', '20.000');
INSERT INTO `gu_conctol` VALUES ('9', '万业企业', '600641', 'http://hq.sinajs.cn/list=sh600641', '14.000', '12.000');
INSERT INTO `gu_conctol` VALUES ('10', '航天电子', '600879', 'http://hq.sinajs.cn/list=sh600879', '8.000', '10.000');

-- ----------------------------
-- Table structure for gu_info
-- ----------------------------
DROP TABLE IF EXISTS `gu_info`;
CREATE TABLE `gu_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `gu_name` varchar(50) DEFAULT NULL,
  `gu_num` int(6) unsigned zerofill DEFAULT NULL,
  `gu_price` double(10,4) DEFAULT NULL,
  `create_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=283 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of gu_info
-- ----------------------------
INSERT INTO `gu_info` VALUES ('262', '振华股份', '603067', '13.8520', '2017-11-30 00:00:00');
INSERT INTO `gu_info` VALUES ('263', '京能置业', '600791', '7.2830', '2017-11-30 00:00:00');
INSERT INTO `gu_info` VALUES ('264', '至纯科技', '603690', '20.1800', '2017-11-30 00:00:00');
INSERT INTO `gu_info` VALUES ('265', '宝钛股份', '600456', '20.3400', '2017-11-30 00:00:00');
INSERT INTO `gu_info` VALUES ('266', '西部建设', '002302', '17.8300', '2017-11-30 00:00:00');
INSERT INTO `gu_info` VALUES ('267', '万业企业', '600641', '12.7800', '2017-11-30 00:00:00');
INSERT INTO `gu_info` VALUES ('268', '航天电子', '600879', '7.9400', '2017-11-30 00:00:00');
INSERT INTO `gu_info` VALUES ('269', '振华股份', '603067', '13.6500', '2017-11-30 00:00:00');
INSERT INTO `gu_info` VALUES ('270', '京能置业', '600791', '7.2200', '2017-11-30 00:00:00');
INSERT INTO `gu_info` VALUES ('271', '至纯科技', '603690', '20.1800', '2017-11-30 00:00:00');
INSERT INTO `gu_info` VALUES ('272', '宝钛股份', '600456', '20.3400', '2017-11-30 00:00:00');
INSERT INTO `gu_info` VALUES ('273', '西部建设', '002302', '17.8300', '2017-11-30 00:00:00');
INSERT INTO `gu_info` VALUES ('274', '万业企业', '600641', '12.7800', '2017-11-30 00:00:00');
INSERT INTO `gu_info` VALUES ('275', '航天电子', '600879', '7.9400', '2017-11-30 00:00:00');
INSERT INTO `gu_info` VALUES ('276', '振华股份', '603067', '13.7200', '2017-12-01 00:00:00');
INSERT INTO `gu_info` VALUES ('277', '京能置业', '600791', '7.2400', '2017-12-01 00:00:00');
INSERT INTO `gu_info` VALUES ('278', '至纯科技', '603690', '21.1800', '2017-12-01 00:00:00');
INSERT INTO `gu_info` VALUES ('279', '宝钛股份', '600456', '20.3500', '2017-12-01 00:00:00');
INSERT INTO `gu_info` VALUES ('280', '西部建设', '002302', '17.5700', '2017-12-01 00:00:00');
INSERT INTO `gu_info` VALUES ('281', '万业企业', '600641', '13.0800', '2017-12-01 00:00:00');
INSERT INTO `gu_info` VALUES ('282', '航天电子', '600879', '7.9500', '2017-12-01 00:00:00');

-- ----------------------------
-- Table structure for gu_user
-- ----------------------------
DROP TABLE IF EXISTS `gu_user`;
CREATE TABLE `gu_user` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `gu_num` int(6) unsigned zerofill DEFAULT NULL,
  `price` double(10,3) DEFAULT NULL,
  `number` int(10) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of gu_user
-- ----------------------------
INSERT INTO `gu_user` VALUES ('12', '600791', '7.283', '1600', '2017-11-30 11:27:20');
INSERT INTO `gu_user` VALUES ('13', '603067', '13.852', '1000', '2017-11-30 11:27:20');

-- ----------------------------
-- Table structure for vip_book
-- ----------------------------
DROP TABLE IF EXISTS `vip_book`;
CREATE TABLE `vip_book` (
  `id` int(10) NOT NULL,
  `vip_num` int(255) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `total_rate` double(10,6) DEFAULT NULL,
  `user_rate` double(10,6) DEFAULT NULL,
  `money` double(20,6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of vip_book
-- ----------------------------

-- ----------------------------
-- Table structure for vip_info
-- ----------------------------
DROP TABLE IF EXISTS `vip_info`;
CREATE TABLE `vip_info` (
  `id` int(11) NOT NULL,
  `vip_project` varchar(255) DEFAULT NULL,
  `vip_num` int(255) DEFAULT NULL,
  `umoney` double(20,6) DEFAULT NULL,
  `create_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of vip_info
-- ----------------------------
