#include <string>
using namespace std;

#include <Security/Security.h>
#include <Security/SecCertificate.h>

int getCacertsFromKeychain(X509_STORE *store) {
  CFArrayRef anchors;
  int ret, err;

  ret = SecTrustCopyAnchorCertificates(&anchors);
  if( ret != 0 ) {
    //could not access root certificates list
    return 1;
  }

  for (int i = 0; i < CFArrayGetCount(anchors); i++) {
    CFDataRef certref;

    SecCertificateRef cr = (SecCertificateRef)CFArrayGetValueAtIndex(anchors, i);

    CSSM_DATA certData;
    int a = SecCertificateGetData(cr, &certData);
    X509 *cert = d2i_X509(NULL, (const unsigned char **)&certData.Data, certData.Length);

    if (X509_STORE_add_cert(store, (X509 *)cert) != 1) {
      X509_free(cert);
      CFRelease(anchors);
      //could not add root certificate to chain
      return 2;
    }
    X509_free(cert);
  }

  CFRelease(anchors);

  return 0;
}

