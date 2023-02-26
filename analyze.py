import pandas as pd



df = pd.read_csv("questionstagRwithoutdupls4.csv")
top_viewed = df.nlargest(5, 'up_vote_count')[['title', 'up_vote_count']]
print("Top 5 most viewed questions:")
for i, row in top_viewed.iterrows():
    print(f"{i + 1}. {row['title']} ({row['up_vote_count']} upvotes)")




"""

def get mean:
    mean_view_count = df['view_count'].mean()
    mean_upvote_count = df['up_vote_count'].mean()
    mean_downvote_count = df['down_vote_count'].mean()
    mean_score = df['score'].mean()
    
    print(f"mean_view_count:{mean_view_count}"
          f" mean_upvote_count:{mean_upvote_count} "
          f"mean_downvote_count:{mean_downvote_count} "
          f"mean_score:{mean_score}")






get top 10:
        user_counts = df.groupby(['owner_user_id', 'owner_display_name']).size().reset_index(name='question_count')
        top_10_users = user_counts.sort_values(by='question_count', ascending=False).head(10)
        for index, row in top_10_users.iterrows():
            print("User ID:", row['owner_user_id'])
            print("Display name:", row['owner_display_name'])
            print("Question count:", row['question_count'])
            print()






get the oldest question
    oldest_question = df.sort_values(by='creation_date', ascending=True).iloc[0]
    print("Question ID:", oldest_question['question_id'])
    print("Question title:", oldest_question['title'])
    print("Question creation date:", oldest_question['creation_date'])





get how many questions are answered 
    is_answered_counts = df['is_answered'].value_counts()
    print("Number of answered questions:", is_answered_counts[True])
    print("Number of answered questions:", is_answered_counts[False])





get number of questions without an accepted answer
    unanswered_questions = df[df['accepted_answer_id'] == 0].shape[0]
    print("Number of unanswered questions:", unanswered_questions)
    
    
    

get top 5 most viewed questions
    top_viewed = df.nlargest(5, 'view_count')[['title', 'view_count']]
    print("Top 5 most viewed questions:")
    for i, row in top_viewed.iterrows():
        print(f"{i + 1}. {row['title']} ({row['view_count']} views)")




"""




