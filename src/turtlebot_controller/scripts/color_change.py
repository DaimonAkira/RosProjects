 import rospy
      from turtlesim.msg import Color


      def change_background_color_client():


              rospy.wait_for_service('/clear')

              try: 

                rospy.set_param('/turtlesim/background_r' , 255)
                rospy.set_param('/turtlesim/background_g' , 0)
                rospy.set_param('/turtlesim/background_b' , 0)

                change_background_color = rospy.ServiceProxy('/clear', Empty)

                resp = change_background_color()

                return resp

              except rospy.ServiceException as e:
               rospy.loginfo(f'Service failed with the exception {e}')


            if __name__ == "__main__" :

              change_background_color_client()