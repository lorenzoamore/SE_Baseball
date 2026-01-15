from database.DB_connect import DBConnect
from model.team import Team
class DAO:
    @staticmethod
    def query_esempio():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select name
                    from team
                    where year = %s """

        cursor.execute(query)

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def load_anni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select year
                    from team
                    where year >= 1980
                    group by year"""
        cursor.execute(query)
        for row in cursor:
            result.append(row['year'])
        cursor.close()
        conn.close()
        return list(result)

    @staticmethod
    def load_squadre(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select t.name, t.team_code, sum(s.salary) as salary
                    from team t, salary s
                    where s.year = %s and t.team_code = s.team_code and t.year = s.year
                    group by t.name, t.team_code """

        cursor.execute(query,(anno,))

        for row in cursor:
            team = Team(
                name=row['name'],
                team_code=row['team_code'],
                salary=row['salary']
            )
            result.append(team)
        return result