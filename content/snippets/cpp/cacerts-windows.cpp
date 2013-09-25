#include <string>
using namespace std;

#include <wincrypt.h>

int getCacertsStringFromFile(X509_STORE *store)
{
  HCERTSTORE hCertStore = CertOpenStore( CERT_STORE_PROV_SYSTEM_W, 0, NULL,
  CERT_SYSTEM_STORE_CURRENT_USER | CERT_STORE_READONLY_FLAG, L"Root");

  if(!hCertStore) {
    std::ostringstream msg;
    msg << "couldn't open certificate store, system error " << GetLastError();
    return 1;
  }

  PCCERT_CONTEXT pCertContext = CertEnumCertificatesInStore(hCertStore, NULL);
  while ( pCertContext ) {
    X509 *cert = d2i_X509(NULL, (const unsigned char **)&pCertContext->pbCertEncoded, pCertContext->cbCertEncoded);
    if (X509_STORE_add_cert(store, (X509 *)cert) != 1) {
      unsigned long err2;
      string errStr("Could not add certificate from store: ");
      err2 = ERR_get_error();
      /* continue if error == certificate already in store */
      if(ERR_GET_REASON(err2) != 101) {
        while(err2 != 0) {
          std::ostringstream res;
          res << err2;
          res << " number=";
          res << ERR_GET_LIB(err2);
          res << ", function=";
          res << ERR_GET_FUNC(err2);
          res << ", reason code=";
          res << ERR_GET_REASON(err2);
          res << "\n";
          errStr += res.str();
          err2 = ERR_get_error();
        };
        return 2;
      }
    }

    pCertContext = CertEnumCertificatesInStore(hCertStore, pCertContext);
  }
  return 0;
}
