SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[fruits_and_vegetables](
	[name] [nvarchar](20) NOT NULL,
	[type] [nvarchar](20) NOT NULL,
	[color] [nvarchar](20) NOT NULL,
	[caloric] [smallint] NOT NULL,
	[description] [nvarchar](200) NOT NULL
) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
ALTER TABLE [dbo].[fruits_and_vegetables] ADD PRIMARY KEY CLUSTERED 
(
	[name] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO

INSERT INTO fruits_and_vegetables (name, type, color, caloric, description) VALUES ('ананас', 'фрукт', 'желтый', 50, 'похож на маленькую пальму');
INSERT INTO fruits_and_vegetables (name, type, color, caloric, description) VALUES ('апельсин', 'фрукт', 'оранжевый', 47, 'это и цвет и фрукт одновременно');
INSERT INTO fruits_and_vegetables (name, type, color, caloric, description) VALUES ('баклажан', 'овощь', 'черный', 25, 'отлично сочетается с чесночным соусом');
INSERT INTO fruits_and_vegetables (name, type, color, caloric, description) VALUES ('болгарский перец', 'овощь', 'желтый', 20, 'выращен болгарами в болгарии');
INSERT INTO fruits_and_vegetables (name, type, color, caloric, description) VALUES ('кабачок', 'овощь', 'зеленый', 24, 'тоже можно есть иногда');
INSERT INTO fruits_and_vegetables (name, type, color, caloric, description) VALUES ('пастернак', 'овощь', 'белый', 75, 'вообще фиг знает что это такое');
INSERT INTO fruits_and_vegetables (name, type, color, caloric, description) VALUES ('патисон', 'овощь', 'белый', 18, 'был популярен у советских дачников');
INSERT INTO fruits_and_vegetables (name, type, color, caloric, description) VALUES ('свекла', 'овощь', 'фиолетовый', 43, 'высокий гликемический индекс');
INSERT INTO fruits_and_vegetables (name, type, color, caloric, description) VALUES ('тыква', 'овощь', 'желтый', 26, 'вкусно запекать в духовке ');
INSERT INTO fruits_and_vegetables (name, type, color, caloric, description) VALUES ('яблоко', 'фрукт', 'зеленый', 52, 'хорошее вкусное яблоко богато железом');
