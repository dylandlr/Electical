import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from textblob import TextBlob
import re

class DataPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()
        
    def clean_text(self, text):
        """Clean text data by removing special characters and normalizing"""
        if isinstance(text, str):
            # Remove special characters and convert to lowercase
            text = re.sub(r'[^\w\s]', '', text.lower())
            return text.strip()
        return ''

    def get_sentiment_score(self, text):
        """Calculate sentiment score for text using TextBlob"""
        try:
            return TextBlob(str(text)).sentiment.polarity
        except:
            return 0.0

    def process_social_media_data(self, df):
        """Process social media data including sentiment analysis"""
        df = df.copy()
        
        # Clean text content
        df['cleaned_text'] = df['content'].apply(self.clean_text)
        
        # Add sentiment scores
        df['sentiment_score'] = df['cleaned_text'].apply(self.get_sentiment_score)
        
        # Process engagement metrics
        engagement_cols = ['likes', 'shares', 'comments']
        for col in engagement_cols:
            if col in df.columns:
                df[col] = df[col].fillna(0)
                df[f'{col}_scaled'] = self.scaler.fit_transform(df[[col]])
        
        return df

    def process_polling_data(self, df):
        """Process polling data with standardization and cleaning"""
        df = df.copy()
        
        # Handle only numeric columns
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        
        # Replace infinite values with NaN for numeric columns only
        df[numeric_cols] = df[numeric_cols].replace([np.inf, -np.inf], np.nan)
        
        # Fill NaN values with mean for numeric columns only
        for col in numeric_cols:
            df[col] = df[col].fillna(df[col].mean())
            if df[col].std() > 0:  # Only scale if there's variance
                df[f'{col}_scaled'] = self.scaler.fit_transform(df[[col]])
        
        return df

    def process_stock_data(self, df):
        """Process stock market data"""
        df = df.copy()
        
        # Calculate daily returns
        df['daily_return'] = df['close'].pct_change()
        
        # Calculate moving averages
        df['MA5'] = df['close'].rolling(window=5).mean()
        df['MA20'] = df['close'].rolling(window=20).mean()
        
        # Calculate volatility
        df['volatility'] = df['daily_return'].rolling(window=20).std()
        
        # Fill NaN values created by rolling calculations
        df = df.fillna(method='bfill')
        
        return df

    def process_election_results(self, df):
        """Process historical election results data"""
        df = df.copy()
        
        # Calculate vote percentages
        if 'total_votes' in df.columns:
            vote_cols = [col for col in df.columns if 'votes' in col.lower() and col != 'total_votes']
            for col in vote_cols:
                df[f'{col}_percentage'] = (df[col] / df['total_votes']) * 100
        
        # Scale numerical features
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
        df[numeric_cols] = self.scaler.fit_transform(df[numeric_cols])
        
        return df

    def combine_features(self, social_df, polling_df, stock_df, election_df):
        """Combine features from different data sources"""
        # Implement feature combination logic based on common keys (dates, regions, etc.)
        # This method should be customized based on specific requirements
        pass