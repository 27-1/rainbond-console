
-- 2019-03-27创建云市应用升级前备份数据表


CREATE TABLE `market_service_data_backup` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `data_backup_id` varchar(32),
  `service_id` varchar(32),
  `tenant_id` varchar(32),
  `group_version` varchar(32),
  `service_template` text DEFAULT NULL,
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8;