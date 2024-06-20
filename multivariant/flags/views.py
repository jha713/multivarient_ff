# flags/views.py
from featureflags.client import CfClient
from featureflags.evaluations.auth_target import Target
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status , generics
import logging

# Initialize logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Initialize the Feature Flags Client
api_key = '4ee6bfa5-8de0-4bca-bb6c-d0cc5f8e8ed5'
#api_key = '2351c0b5-f2e6-4b2d-be5c-c858f242b6a1'
cf = CfClient(api_key)
cf.wait_for_initialization()

class FeatureFlagView(APIView):
    def get(self, request, user_email):
        logger.debug(f"Received request for user_email: {user_email}")
        try:

            # Define the flag key and target details
            flag_key = 'multivariant'
            #flag_key ='multivariance'
            target_identifier = user_email
            target_name = 'group'
            target = Target(identifier=target_identifier, name=target_name)
            
            # Get the feature flag variation for the target user
            variation = cf.string_variation(flag_key, target, default='default')
            logger.debug(f"Variation for {user_email}: {variation}")
            
            # Return the feature flag variation as a response
            return Response({"variation": variation}, status=status.HTTP_200_OK)
        
        except Exception as e:
            logger.error(f"Error fetching variation: {e}")
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
