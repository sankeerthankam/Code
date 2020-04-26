# This one counts, for each score, the number of distinct greater or equal scores.
# https://leetcode.com/problems/rank-scores/discuss/456610/MySQL-Two-Simple-Solutions-and-Explanations-for-Beginners
# Check Rank, Dense Rank and Row Num tutorial as extended knowledge
# Write your MySQL query statement below

SELECT 
    s1.Score, COUNT(s2.Score) as Rank
FROM    
    Scores s1, (SELECT DISTINCT Score from Scores) s2
WHERE 
    s1.Score <= s2.Score
GROUP BY s1.Id
ORDER BY 1 DESC
