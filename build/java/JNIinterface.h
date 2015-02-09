/* DO NOT EDIT THIS FILE - it is machine generated */
#include <jni.h>
/* Header for class JNIinterface */

#ifndef _Included_JNIinterface
#define _Included_JNIinterface
#ifdef __cplusplus
extern "C" {
#endif
/*
 * Class:     JNIinterface
 * Method:    cocoEvaluateFunction
 * Signature: (LProblem;[D)[D
 */
JNIEXPORT jdoubleArray JNICALL Java_JNIinterface_cocoEvaluateFunction
  (JNIEnv *, jclass, jobject, jdoubleArray);

/*
 * Class:     JNIinterface
 * Method:    cocoGetNumberOfVariables
 * Signature: (LProblem;)I
 */
JNIEXPORT jint JNICALL Java_JNIinterface_cocoGetNumberOfVariables
  (JNIEnv *, jclass, jobject);

/*
 * Class:     JNIinterface
 * Method:    cocoGetNumberOfObjectives
 * Signature: (LProblem;)I
 */
JNIEXPORT jint JNICALL Java_JNIinterface_cocoGetNumberOfObjectives
  (JNIEnv *, jclass, jobject);

/*
 * Class:     JNIinterface
 * Method:    cocoGetSmallestValuesOfInterest
 * Signature: (LProblem;)[D
 */
JNIEXPORT jdoubleArray JNICALL Java_JNIinterface_cocoGetSmallestValuesOfInterest
  (JNIEnv *, jclass, jobject);

/*
 * Class:     JNIinterface
 * Method:    cocoGetLargestValuesOfInterest
 * Signature: (LProblem;)[D
 */
JNIEXPORT jdoubleArray JNICALL Java_JNIinterface_cocoGetLargestValuesOfInterest
  (JNIEnv *, jclass, jobject);
    
/*
 * Class:     JNIinterface
 * Method:    cocoGetLargestValuesOfInterest
 * Signature: (LProblem;)[D
 */
JNIEXPORT jdoubleArray JNICALL Java_JNIinterface_cocoGetLargestValuesOfInterest
    (JNIEnv *, jclass, jobject);
    
/*
 * Class:     JNIinterface
 * Method:    validProblem
 * Signature: (Ljava/lang/String;I)Z
 */
JNIEXPORT jboolean JNICALL Java_JNIinterface_validProblem
    (JNIEnv *, jclass, jstring, jint);
    
/*
 * Class:     JNIinterface
 * Method:    cocoGetProblemId
 * Signature: (LProblem;)Ljava/lang/String;
 */
JNIEXPORT jstring JNICALL Java_JNIinterface_cocoGetProblemId
    (JNIEnv *, jclass, jobject);


#ifdef __cplusplus
}
#endif
#endif
